from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    role = forms.ChoiceField(
        choices=[('student', 'Student'), ('lecturer', 'Lecturer'), ('admin', 'Admin')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

"""
from django import forms
from django.contrib.auth.hashers import make_password
from .models import Student

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["StudentNumber", "FirstName", "LastName", "Email"]

    def save(self, commit=True):
        student = super().save(commit=False)
        student.username = student.Email   
        student.set_password(student.LastName)  # Use set_password    
        student.save()
        return student

class LecturerRegisterForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('StaffNumber', 'FirstName', 'LastName', 'Email', 'Department')

    def save(self, commit=True):
        lecturer = super().save(commit=False)
        lecturer.username = lecturer.Email
        lecturer.password = make_password(lecturer.LastName)
        lecturer.save()
        return lecturer

 """