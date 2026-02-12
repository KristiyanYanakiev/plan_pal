from django.contrib import admin
from django.contrib.admin import ModelAdmin

from friends.models import Friend


@admin.register(Friend)
class FriendAdmin(ModelAdmin):
    pass
