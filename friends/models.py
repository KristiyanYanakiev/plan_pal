from django.db import models

from common.mixins import TimeStampModel
from friends.validators import validate_image_size


class Friend(TimeStampModel):
    name = models.CharField(
        max_length=100,
    )
    photo = models.ImageField(
        blank=True,
        null=True,
        validators=[validate_image_size]
    )


    def __str__(self):
        return self.name


