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


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields='__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields='__all__'
       

