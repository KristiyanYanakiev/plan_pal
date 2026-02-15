from django.db import models

from common.mixins import TimeStampModel


class Proposal(TimeStampModel):
    title = models.CharField(
        max_length=100,
    )
    type_of_activity = models.CharField(
        max_length=100,
        help_text='Please enter the type of activity, e.g. "Eating out", "Bowling ect."'
    )

    place_of_event = models.URLField(
        null=True,
        blank=True,
        help_text='If you want, you can include a link to check the place:'
    )
    proposed_date_and_time = models.DateTimeField(
        help_text='Please enter the proposed date and time of the event: '
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )


    def __str__(self):
        return f"{self.title} ({self.status})"


