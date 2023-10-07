from django import forms
from .models import Senior

class SeniorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Senior
        fields = ['name', 'profession', 'expertise', 'experience_years', 'working_in']
