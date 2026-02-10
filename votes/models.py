from django.db import models

class Vote(models.Model):
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE)
    friend = models.ForeignKey('friends.Friend', on_delete=models.CASCADE)
    yes = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['proposal', 'friend'], name='unique_vote_per_friend')
        ]