from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, DeleteView

from accounts.forms import CustomUserCreationForm


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('common:home')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'accounts/logout.html')

    def post(self, request):
        logout(request)
        return redirect('common:home')


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('common:home')

    def get_object(self, queryset=None):
        return self.request.user