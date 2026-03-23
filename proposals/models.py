from django.db import models
from django.conf import settings

class Proposal(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    notes = models.TextField(blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_proposals'
    )

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='proposals'
    )


