from django.contrib.auth import login, authenticate
from mainpages.forms import UserSelectionSignupForm
from mainpages.models import Employer, Applicant, UserProfile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from allauth.socialaccount.forms import SignupForm
import datetime


# Create your views here.



# View for about page template

def update_user_social_data(strategy, *args, **kwargs):
  response = kwargs['response']
  backend = kwargs['backend']
  user = kwargs['user']

  if response['picture']:
    url = response['picture']
    userProfile_obj = UserProfile()
    userProfile_obj.user = user
    userProfile_obj.picture = url
    userProfile_obj.save()
    


def signupPageView(request):
    breakpoint()
    if request.method == 'POST':
        form = UserSelectionSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'homepage/signup.html', {'form': form})

def aboutPageView(request) :
    return render(request, 'applicationpages/about.html') 


# View for the index page

def indexPageView(request) :
    # sOutput = '<html><head><title>Main Page</title></head><body><p>This is the index page' + menu +'</body></html>'
    # return HttpResponse(sOutput) 
   
    return render(request, 'homepage/index.html') 




