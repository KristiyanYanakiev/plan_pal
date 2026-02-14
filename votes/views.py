from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from friends.models import Friend
from proposals.models import Proposal
from votes.models import Vote


def vote_on_proposal(request, proposal_id):
    if request.method != "POST":
        return redirect("proposals:details", pk=proposal_id)

    proposal = get_object_or_404(Proposal, pk=proposal_id)
    friend_id = request.POST.get("friend_id")
    choice = request.POST.get("choice")
    friend = get_object_or_404(Friend, pk=friend_id)
    is_yes = choice == "yes"

    Vote.objects.update_or_create(
        proposal=proposal,
        friend=friend,
        defaults={"yes": is_yes}
    )

    return redirect("proposals:details", pk=proposal_id)
