from django.contrib.auth import login, authenticate
from mainpages.forms import UserSelectionSignupForm
from mainpages.models import Employer, Applicant, JobPosting
from django.shortcuts import render, redirect
from django.http import HttpResponse
from allauth.socialaccount.forms import SignupForm

import datetime


# Create your views here.



# View for about page template

def aboutPageView(request) :
    return render(request, 'applicationpages/about.html') 

def jpPageView(request) :
    context = {'postings' : JobPosting.objects.filter(ispublic=True)}
    return render(request, 'applicationpages/jobpostings.html', context)

# View for the index page

def indexPageView(request) :
    # sOutput = '<html><head><title>Main Page</title></head><body><p>This is the index page' + menu +'</body></html>'
    # return HttpResponse(sOutput) 
   
    return render(request, 'homepage/index.html') 




