from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from friends.models import Friend
from proposals.forms import ProposalForm, ProposalSearchForm
from proposals.models import Proposal


def proposals_list(request: HttpRequest) -> HttpResponse:
    proposal_search_form = ProposalSearchForm(request.GET or None)
    proposals = Proposal.objects.all()

    if 'query' in request.GET:
        if proposal_search_form.is_valid():
            searched_value = proposal_search_form.cleaned_data['query']
            proposals = Proposal.objects.filter(
                Q(title__icontains=searched_value)
                    |
                Q(notes__contains=searched_value)
            )

    context = {
        'proposals': proposals,
        'proposal_search_form': proposal_search_form
    }

    return render(request, 'proposals/list.html', context)

def select_voter(request, pk):
    if request.method == "POST":
        friend_id = request.POST.get("friend_id")
        request.session["active_friend_id"] = friend_id
    return redirect("proposals:details", pk=pk)

from django.shortcuts import get_object_or_404, render
from friends.models import Friend
from proposals.models import Proposal

def proposal_details(request, pk):
    proposal = get_object_or_404(Proposal, pk=pk)

    yes_friends = proposal.participants.filter(votes__proposal=proposal, votes__yes=True)
    no_friends = proposal.participants.filter(votes__proposal=proposal, votes__yes=False)
    not_voted = Friend.objects.exclude(votes__proposal=proposal)

    context = {
        "proposal": proposal,
        "yes_friends": yes_friends,
        "no_friends": no_friends,
        "not_voted": not_voted,
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
