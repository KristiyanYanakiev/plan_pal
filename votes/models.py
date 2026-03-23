from django.conf import settings
from django.db import models
from proposals.models import Proposal


class Vote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    proposal = models.ForeignKey(
        Proposal,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    yes = models.BooleanField()

    class Meta:
        unique_together = ('user', 'proposal')