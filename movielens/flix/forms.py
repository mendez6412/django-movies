from django import forms

class RaterForm(forms.ModelForm):
    # email = forms.EmailField(label="Email")


    class Meta:
        model = Rater
        fields = ['gender', 'age', 'occupation', 'zipcode']
