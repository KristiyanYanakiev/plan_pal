from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from friends.models import FriendGroup
from .forms import ProposalForm
from .models import Proposal

class ProposalListView(LoginRequiredMixin, ListView):
    model = Proposal
    template_name = 'proposals/list.html'

    def get_queryset(self):
        return Proposal.objects.filter(group__owner=self.request.user)

class ProposalCreateView(LoginRequiredMixin, CreateView):
    model = Proposal
    form_class = ProposalForm
    template_name = 'proposals/form.html'
    success_url = reverse_lazy('proposals:list')

    def form_valid(self, form):
        form.instance.group = FriendGroup.objects.filter(owner=self.request.user).first()
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProposalUpdateView(LoginRequiredMixin, UpdateView):
    model = Proposal
    form_class = ProposalForm
    template_name = 'proposals/form.html'
    success_url = reverse_lazy('proposals:list')

class ProposalDeleteView(LoginRequiredMixin, DeleteView):
    model = Proposal
    template_name = 'proposals/delete.html'
    success_url = reverse_lazy('proposals:list')

class ProposalDetailView(LoginRequiredMixin, DetailView):
    model = Proposal
    template_name = 'proposals/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proposal = self.object
        context['yes_friends'] = proposal.group.friends.filter(votes__proposal=proposal, votes__yes=True)
        context['no_friends'] = proposal.group.friends.filter(votes__proposal=proposal, votes__yes=False)
        context['not_voted'] = proposal.group.friends.exclude(votes__proposal=proposal)
        return context