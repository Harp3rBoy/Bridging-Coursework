from django import forms

from .models import PersonalDetails, Education


class PersonalDetailsForm(forms.ModelForm):

    class Meta:
        model = PersonalDetails
        fields = ('name', 'dob', 'email',)


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('institution', 'grades', 'start_date', 'end_date')
