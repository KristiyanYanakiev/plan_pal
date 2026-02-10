from django.db import models

from proposals.choices import ProposalStatusChoices


class Proposal(models.Model):
    title = models.CharField(
        max_length=100,
    )
    type_of_activity = models.CharField(
        max_length=100,
        help_text='Please enter the type of activity, e.g. "Eating out", "Bowling ect."'
    )
    proposed_date_and_time = models.DateTimeField(
        help_text='Please enter the proposed date and time of the event: '
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        choices=ProposalStatusChoices.choices,
        default=ProposalStatusChoices.PROPOSED,
        help_text="Current status of the proposal"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"


