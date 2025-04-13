from django import forms 
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class LecturerForm(forms.ModelForm):
    class Meta:
        model=Lecturer
        fields='__all__'

