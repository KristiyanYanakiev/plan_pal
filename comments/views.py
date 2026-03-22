from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.proposal_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('proposals:details', kwargs={'pk': self.kwargs['pk']})