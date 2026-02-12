from django import forms

from friends.models import Friend


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        exclude = ['created_at', 'updated_at']
