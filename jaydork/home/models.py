from django.db import models

''' Database outline with columns Name, Username, Password, and Email, filled out by the user '''
class Account(models.Model):
	name= models.CharField(max_length=20, default=None)
	username = models.CharField(max_length=15, default=None)
	password= models.CharField(max_length=10, default=None)
	email= models.EmailField(default=None) # Django pre-defined email requirements

