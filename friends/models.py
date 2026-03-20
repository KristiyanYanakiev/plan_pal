from django.db import models
from plan_pal import settings


class FriendGroup(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friend_groups')

    def __str__(self):
        return f"{self.name} ({self.owner.username})"

class Friend(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(FriendGroup, on_delete=models.CASCADE, related_name='friends', blank=True, null=True)

    def __str__(self):
        return self.name

