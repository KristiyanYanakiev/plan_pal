from django.db import models
from friends.models import FriendGroup
from plan_pal import settings


class Proposal(models.Model):
    title = models.CharField(max_length=100)
    group = models.ForeignKey(to=FriendGroup, on_delete=models.CASCADE, related_name='proposals', blank=True, null=True)
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    proposed_date_and_time = models.DateTimeField()
    type_of_activity = models.CharField(max_length=100)
    place_of_event = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.group})"


