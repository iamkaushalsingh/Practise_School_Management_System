from django import forms
from .models import Internship, Application

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['title', 'description', 'salary', 'is_active']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = []
