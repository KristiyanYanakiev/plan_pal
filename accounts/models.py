from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q


# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles', blank=True, null=True)

    def get_friends(self):
        return self.__class__.objects.filter(
            Q(sent_connections__to_user=self, sent_connections__accepted=True) |
            Q(received_connections__from_user=self, received_connections__accepted=True)
        ).distinct()

    def __str__(self):
        return self.username