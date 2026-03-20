from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView

from proposals.models import Proposal


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['past_events'] =Proposal.objects.filter(proposed_date_and_time__lt=timezone.now())
        context['upcoming_events'] = Proposal.objects.filter(proposed_date_and_time__gte=timezone.now())

        return context


class AboutPageView(TemplateView):
    template_name = 'common/about.html'
