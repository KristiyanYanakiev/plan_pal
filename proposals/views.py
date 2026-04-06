from django.contrib.auth.mixins import LoginRequiredMixin
from common.utils import run_in_background
from common.tasks import send_email
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)
from django.shortcuts import get_object_or_404, redirect

from votes.models import Vote
from .models import Proposal
from .forms import ProposalForm


class ProposalListView(LoginRequiredMixin, ListView):
    model = Proposal
    template_name = 'proposals/list.html'
    context_object_name = 'proposals'

    def get_queryset(self):
        user = self.request.user
        qs = Proposal.objects.filter(participants=user).distinct()

        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(title__icontains=query)

        return qs



class ProposalCreateView(LoginRequiredMixin, CreateView):
    model = Proposal
    form_class = ProposalForm
    template_name = 'proposals/form.html'
    success_url = reverse_lazy('proposals:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        form.instance.participants.add(self.request.user)

        emails = [
            user.email for user in form.instance.participants.all()
            if user.email
        ]

        if emails:
            run_in_background(
                send_email,
                "New Proposal",
                f"A new proposal was created: {form.instance.title}",
                emails
            )

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
        return Proposal.objects.filter(
            Q(owner=self.request.user) |
            Q(participants=self.request.user)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        proposal = self.object
        user = self.request.user

        context['user_vote'] = proposal.votes.filter(user=user).first()

        voted_users = proposal.votes.values_list('user_id', flat=True)

        context['not_voted'] = proposal.participants.exclude(
            id__in=voted_users
        ).exclude(
            id=proposal.owner_id
        )

        context['yes_users'] = proposal.votes.filter(yes=True)
        context['no_users'] = proposal.votes.filter(yes=False)

        context['can_vote'] = (
            user != proposal.owner and
            user in proposal.participants.all()
        )

        return context

class VoteView(LoginRequiredMixin, View):
    def post(self, request, pk, value):
        proposal = get_object_or_404(Proposal, pk=pk)
        user = request.user

        if user == proposal.owner:
            return redirect('proposals:details', pk=pk)

        if user not in proposal.participants.all():
            return redirect('proposals:details', pk=pk)

        yes_value = (str(value) == "1")

        Vote.objects.update_or_create(
            user=user,
            proposal=proposal,
            defaults={'yes': yes_value}
        )

        return redirect('proposals:details', pk=pk)