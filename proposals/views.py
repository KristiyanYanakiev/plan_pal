from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.shortcuts import get_object_or_404, redirect

from votes.models import Vote
from .models import Proposal
from .forms import ProposalForm


class ProposalListView(LoginRequiredMixin, ListView):
    model = Proposal
    template_name = 'proposals/list.html'
    context_object_name = 'proposals'

    def get_queryset(self):
        return Proposal.objects.filter(
            participants=self.request.user
        )

class ProposalCreateView(LoginRequiredMixin, CreateView):
    model = Proposal
    form_class = ProposalForm
    template_name = 'proposals/form.html'
    success_url = reverse_lazy('proposals:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user

        response = super().form_valid(form)

        form.instance.participants.add(self.request.user)

        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProposalUpdateView(LoginRequiredMixin, UpdateView):
    model = Proposal
    form_class = ProposalForm
    template_name = 'proposals/form.html'
    success_url = reverse_lazy('proposals:list')

    def get_queryset(self):
        return Proposal.objects.filter(owner=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProposalDeleteView(LoginRequiredMixin, DeleteView):
    model = Proposal
    template_name = 'proposals/delete.html'
    success_url = reverse_lazy('proposals:list')

    def get_queryset(self):
        return Proposal.objects.filter(owner=self.request.user)


class ProposalDetailView(LoginRequiredMixin, DetailView):
    model = Proposal
    template_name = 'proposals/details.html'
    context_object_name = 'proposal'

    def get_queryset(self):
        return Proposal.objects.filter(participants=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proposal = self.object

        context['yes_users'] = proposal.votes.filter(yes=True)
        context['no_users'] = proposal.votes.filter(yes=False)

        voted_users = proposal.votes.values_list('user', flat=True)

        context['not_voted'] = proposal.participants.exclude(id__in=voted_users)

        return context


class VoteView(LoginRequiredMixin, View):

    def post(self, request, pk, value):
        proposal = get_object_or_404(
            Proposal,
            pk=pk,
            participants=request.user
        )

        Vote.objects.update_or_create(
            user=request.user,
            proposal=proposal,
            defaults={'yes': bool(int(value))}
        )

        return redirect('proposals:details', pk=pk)