from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from proposals.models import Proposal
from .models import Comment


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        proposal = get_object_or_404(Proposal, pk=pk)

        if request.user not in proposal.participants.all() and request.user != proposal.owner:
            return redirect('proposals:details', pk=pk)

        text = request.POST.get('text')

        if text:
            Comment.objects.create(
                user=request.user,
                proposal=proposal,
                text=text
            )

        return redirect('proposals:details', pk=pk)


class CommentUpdateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)

        if comment.user != request.user:
            return redirect('proposals:details', pk=comment.proposal_id)

        text = request.POST.get('text')

        if text:
            comment.text = text
            comment.save()

        return redirect('proposals:details', pk=comment.proposal_id)


class CommentDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)

        if comment.user != request.user:
            return redirect('proposals:details', pk=comment.proposal_id)

        proposal_id = comment.proposal_id
        comment.delete()

        return redirect('proposals:details', pk=proposal_id)