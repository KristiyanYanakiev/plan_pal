from django import forms
from friends.models import FriendGroup, Friend


class FriendGroupForm(forms.ModelForm):
    class Meta:
        model = FriendGroup
        exclude = ['owner', 'created_at', 'updated_at']  # owner set automatically in view
        error_messages = {
            'name': {
                'required': 'Please enter a group name.'
            }
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter group name'}),
        }

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name']

class FriendSearchFrom(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False
    )
