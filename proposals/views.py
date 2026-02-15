from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from friends.models import Friend
from proposals.forms import ProposalForm
from proposals.models import Proposal


def proposals_list(request: HttpRequest) -> HttpResponse:
    proposals = Proposal.objects.all()
    context = {
        'proposals': proposals,
    }

    return render(request, 'proposals/list.html', context)

def select_voter(request, pk):
    if request.method == "POST":
        friend_id = request.POST.get("friend_id")
        request.session["active_friend_id"] = friend_id
    return redirect("proposals:details", pk=pk)

def proposal_details(request, pk):
    proposal = get_object_or_404(Proposal, pk=pk)
    friends = Friend.objects.all()

    voted_friend_ids = set(proposal.votes.values_list("friend_id", flat=True))

    context = {
        "proposal": proposal,
        "friends": friends,
        "voted_friend_ids": voted_friend_ids,
    }

    return render(request, "proposals/details.html", context)


def create_proposal(request: HttpRequest) -> HttpResponse:
    form = ProposalForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('proposals:list')

    context = {
            'form': form,
        }

    return render(request, 'proposals/create.html', context)

def edit_proposal(request: HttpRequest, pk) -> HttpResponse:
    proposal = get_object_or_404(Proposal, pk=pk)
    form = ProposalForm(request.POST or None, instance=proposal)

    if request.method == 'POST' and form.is_valid():
        instance = form.save()
        return redirect('proposals:details', pk=instance.pk)

    context = {
        'proposal': proposal,
        'form': form,
    }
    return render(request, 'proposals/edit.html', context)

def delete_proposal(request: HttpRequest, pk) -> HttpResponse:
    proposal = get_object_or_404(Proposal, pk=pk)

    if request.method == 'POST':
        proposal.delete()
        return redirect('proposals:list')

    context = {
        'proposal': proposal,
    }
    return render(request, 'proposals/delete.html', context)
