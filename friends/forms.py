from django import forms


class FriendSearchFrom(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False
    )
