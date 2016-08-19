from django import forms
from django.contrib.auth.models import Rater
from django.contrib.auth.forms import UserCreationForm

class RaterForm(UserCreationForm):
    gender = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    occupation = forms.IntegerField(required=True)
    zipcode = forms.CharField(required=True)
    user = forms.

    class Meta:
        model = Rater
        fields =
