from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'required': True, 
        'placeholder': 'Username'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'required': True, 
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'required': True, 
        'placeholder': 'Last Name'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'required': True, 
        'placeholder': 'Phone Number'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'required': True, 
        'placeholder': 'Address'
    }))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        'required': True,
        'type': 'date'
    }))
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, widget=forms.RadioSelect)
    public_visibility = forms.BooleanField(required=False)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'required': True, 
        'placeholder': 'Enter your email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': True, 
        'placeholder': 'Enter your password',
        'id': 'password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': True, 
        'placeholder': 'Confirm Password',
        'id': 'confirmPassword'
    }))

    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'phone_number',
            'address', 'birth_date', 'user_type', 'public_visibility',
            'email', 'password1', 'password2'
        ]


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'required': True,
        'placeholder': 'Enter your email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': True, 
        'placeholder': 'Enter your password'
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
