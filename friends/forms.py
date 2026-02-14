from django import forms

from friends.models import Friend


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        exclude = ['created_at', 'updated_at']
        error_messages = {
            'name': {
                'required': 'Please enter a name.'
            }
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

