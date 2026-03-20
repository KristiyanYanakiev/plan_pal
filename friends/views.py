from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import FriendGroupForm, FriendForm
from .models import FriendGroup, Friend


class FriendGroupListView(LoginRequiredMixin, ListView):
    model = FriendGroup
    template_name = 'friends/group_list.html'

    def get_queryset(self):
        return FriendGroup.objects.filter(owner=self.request.user)

class FriendGroupCreateView(LoginRequiredMixin, CreateView):
    model = FriendGroup
    form_class = FriendGroupForm
    template_name = 'friends/group_form.html'
    success_url = reverse_lazy('friends:group-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class FriendGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = FriendGroup
    form_class = FriendGroupForm
    template_name = 'friends/group_form.html'
    success_url = reverse_lazy('friends:group-list')

class FriendGroupDeleteView(LoginRequiredMixin, DeleteView):
    model = FriendGroup
    template_name = 'friends/group_delete.html'
    success_url = reverse_lazy('friends:group-list')


class FriendListView(LoginRequiredMixin, ListView):
    model = Friend
    template_name = 'friends/list.html'

    def get_queryset(self):
        return Friend.objects.filter(group__owner=self.request.user)

class FriendCreateView(LoginRequiredMixin, CreateView):
    model = Friend
    form_class = FriendForm
    template_name = 'friends/form.html'
    success_url = reverse_lazy('friends:list')

    def form_valid(self, form):
        group = FriendGroup.objects.filter(owner=self.request.user).first()
        form.instance.group = group
        return super().form_valid(form)

class FriendUpdateView(LoginRequiredMixin, UpdateView):
    model = Friend
    form_class = FriendForm
    template_name = 'friends/form.html'
    success_url = reverse_lazy('friends:list')

class FriendDeleteView(LoginRequiredMixin, DeleteView):
    model = Friend
    template_name = 'friends/delete.html'
    success_url = reverse_lazy('friends:list')
