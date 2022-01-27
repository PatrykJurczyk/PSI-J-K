from django import forms
from .models import Uzytkownik
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Uzytkownik
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = Uzytkownik.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Niepoprawna nazwa użytkownika")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Uzytkownik.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Niepoprawny email")
        return email

    def clean_password1(self):
        pass1 = self.cleaned_data.get('password1')
        return pass1

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError("Hasła się różnią")
        return pass1

