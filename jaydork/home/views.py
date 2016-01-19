from home.youtube_upload import get_upload_list
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AccountCreate, SignIn
from .models import Account


''' Each function return the html template with additional information depending on the page'''

def home_page(request):
	return render(request, 'view.html')

def bio(request):

	return render(request, 'bio.html')

def videos(request):
	videos = get_upload_list() # runs function, returns list 
	return render(request, 'videos.html', {
		'videos' : videos #lets me use the list "videos" in the html
		})




























































































































































































def games(request):
	return render(request, 'games.html')

def signin(request):
	if request.method=='POST':
		form = SignIn(request.POST) 
		if form.is_valid(): #Checks if input exists (only requires input box to have something in it)
			#checks that username and password are in database, will always pass at the moment
			Account.objects.filter(username='username', password='password').exists() 
			return HttpResponseRedirect('games.html') #redirect to games page
	else: form = SignIn()

	return render(request, 'signin.html', {'form':form})

def create_acct(request):
	if request.method=='POST':
		form = AccountCreate(request.POST) #creates a user account
		if form.is_valid(): #checks all fields are filled in
			form.save() # saves user account to database
			return HttpResponseRedirect('games.html') #redirects to games page
	else:
		form = AccountCreate()

	return render(request, 'create_acct.html', {'form':form})