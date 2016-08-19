from django import forms
from django.contrib.auth.models import Rater
from django.contrib.auth.forms import UserCreationForm

class RaterForm(forms.ModelForm):
    # email = forms.EmailField(label="Email")


    class Meta:
        model = Rater
        fields = ['gender', 'age', 'occupation', 'zipcode']
