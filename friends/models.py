from django.db import models

from friends.validators import validate_image_size


class Friend(models.Model):
    name = models.CharField(
        max_length=100,
    )
    photo = models.ImageField(
        upload_to='media',
        blank=True,
        null=True,
        validators=[validate_image_size]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


