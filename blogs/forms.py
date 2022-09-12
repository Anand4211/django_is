from django import forms
from blogs.models import Poost
class PoostForm(forms.ModelForm):
    class Meta:
        model=Poost
        fields="__all__"