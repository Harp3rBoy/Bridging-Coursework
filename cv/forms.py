from django import forms

from .models import PersonalDetails


class DetailsForm(forms.ModelForm):

    class Meta:
        model = PersonalDetails
        fields = ('name', 'dob', 'email',)
