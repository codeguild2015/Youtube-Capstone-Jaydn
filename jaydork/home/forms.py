from django import forms
from home import models

class AccountCreate(forms.ModelForm): # Used to create an account
	password = forms.CharField(widget=forms.PasswordInput) # hides password input
	confirm_password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = models.Account # stores required information from database outline
		#what will show up on screen for the user
		fields = ['name','username','password', 'confirm_password','email'] 

class SignIn(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = models.Account
		fields = ['username','password']