from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=100, help_text="Required, Enter a valid email address!")
    phone = forms.CharField(widget=forms.NumberInput())
    dob = forms.DateField(label="Date of birth", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Account
        fields = ("name", "phone", "email", "password1", "password2", "dob", "gender")

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'id': 'loginPassword'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'id': 'loginEmail', 'autocomplete': 'off'}))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Login")

class UserUpdateForm(forms.ModelForm):

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )

    phone = forms.CharField(label="Phone Number", widget=forms.NumberInput(attrs={'id': 'dashboardPhone'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'id': 'dashboardEmail'}))
    dob = forms.DateField(label="Date of birth", widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(label="Gender", choices=gender_choices, widget=forms.Select(attrs={'id': 'dashboardPlasma'}))
    
    class Meta:
        model = Account
        fields = ["email", "phone", "gender"]
