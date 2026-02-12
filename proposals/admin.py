from django.contrib import admin

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from proposals.models import Proposal


@admin.register(Proposal)
class ProposalAdmin(ModelAdmin):
    exclude = ['attendees']

