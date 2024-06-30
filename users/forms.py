from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'focus:outline-none','placeholder':'demo@gmail.com'}))
    user_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class': 'focus:outline-none','placeholder':'Paulie_Smith'}))
    password1 = forms.CharField(max_length=30, required=True,widget=forms.PasswordInput(attrs={'class': 'focus:outline-none',}))
    password2 = forms.CharField(max_length=30, required=True,widget=forms.PasswordInput(attrs={'class': 'focus:outline-none',}))
    class Meta:
        model=User
        fields=("email", "user_name", "password1", "password2")
    def save(self, commit=True):
        User=super(SignUpForm, self).save(commit=False)
        User.email=self.cleaned_data["email"]
        User.username=self.cleaned_data["user_name"]
        if commit:
            User.save()
        return User