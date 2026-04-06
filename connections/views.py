from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.views.generic import ListView

from .models import Connection

User = get_user_model()


class SendConnectionRequestView(LoginRequiredMixin, View):
    def post(self, request, user_id):
        to_user = get_object_or_404(User, id=user_id)

        Connection.objects.get_or_create(
            from_user=request.user,
            to_user=to_user
        )

        return redirect('common:home')


class AcceptConnectionRequestView(LoginRequiredMixin, View):
    def post(self, request, connection_id):
        connection = get_object_or_404(
            Connection,
            id=connection_id,
            to_user=request.user
        )

        connection.accepted = True
        connection.save()

        return redirect('common:home')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'connections/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)


class PendingRequestsView(LoginRequiredMixin, ListView):
    model = Connection
    template_name = 'connections/pending.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return Connection.objects.filter(
            to_user=self.request.user,
            accepted=False
        )