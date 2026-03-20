from django.db import models

from friends.models import Friend
from proposals.models import Proposal


class Vote(models.Model):
    proposal = models.ForeignKey(to=Proposal, on_delete=models.CASCADE)
    friend = models.ForeignKey(to=Friend, on_delete=models.CASCADE)
    yes = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['proposal', 'friend'], name='unique_vote_per_friend')
        ]