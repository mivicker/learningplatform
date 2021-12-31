from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "role",
            "pronouns",
            "team",
            "buddy",
        ]
