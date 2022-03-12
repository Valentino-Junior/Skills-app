from django import forms
from .models import Profile


class UploadForm(forms.ModelForm):
    potrait = forms.ImageField()
    class Meta:
        model = Profile
        fields = ('name', 'description', 'potrait', 'skill')
