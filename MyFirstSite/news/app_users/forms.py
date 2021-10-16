from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
	last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
	phone = forms.CharField(required=False, help_text='Телефон')
	city = forms.CharField(max_length=36, required=False, help_text='Город')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'phone', 'city', 'password1', 'password2',)