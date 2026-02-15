from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone

from proposals.models import Proposal


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:

    past_proposals = Proposal.objects.filter(proposed_date_and_time__lt=timezone.now())
    upcoming_proposals = Proposal.objects.filter(proposed_date_and_time__gte=timezone.now())

    context = {
        'past_events': past_proposals,
        'upcoming_events': upcoming_proposals
    }

    return render(request, 'common/home.html', context)

def about_page(request: HttpRequest) -> HttpResponse:

    return render(request, 'common/about.html')
