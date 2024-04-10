from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import StudentProfile, TeacherProfile

class StudentRegistrationForm(UserCreationForm):
    registration_number = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=15)
    department = forms.CharField(max_length=100)
    batch = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'registration_number', 'address', 'phone', 'department', 'batch']

class TeacherRegistrationForm(UserCreationForm):
    teacher_id = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=15)
    department = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'teacher_id', 'address', 'phone', 'department']

class StudentProfileForm(UserChangeForm):
    class Meta:
        model = StudentProfile
        fields = ['registration_number', 'address', 'phone', 'department', 'batch']

class TeacherProfileForm(UserChangeForm):
    class Meta:
        model = TeacherProfile
        fields = ['teacher_id', 'address', 'phone', 'department']
