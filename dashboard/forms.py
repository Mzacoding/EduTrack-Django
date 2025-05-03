from django import forms

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
