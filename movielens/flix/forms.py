from django import forms
from .models import Rater, Rating


class RaterForm(forms.ModelForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = Rater
        fields = ['gender', 'age', 'occupation', 'zipcode']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
