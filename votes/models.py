from django.db import models

class Vote(models.Model):
    proposal = models.ForeignKey('proposals.Proposal', on_delete=models.CASCADE, related_name='votes')
    friend = models.ForeignKey('friends.Friend', on_delete=models.CASCADE, related_name='votes')
    yes = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['proposal', 'friend'], name='unique_vote_per_friend')
        ]