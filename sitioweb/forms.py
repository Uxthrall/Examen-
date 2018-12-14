from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput




class UserForm(forms.ModelForm):
	class Meta():
		# password=widget=forms.TextInput(attrs={'type':'password'})
		model = User
		fields=('username','password','email')
		help_texts={
				'username':None,
				'email':None,
		}
		widgets = {
			'password':TextInput(attrs={'type':'password'})
		}

