from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def newsletterPageView(request) :
    return render(request, 'management/newsletter.html')

def showsendPageView(request):
    return render(request, 'management/newsletterredirect.html')

def usersPageView(request) :
    content = {

        "random" : random.randrange(3, 20),
        "random1" : random.randrange(3, 6),
        "random2" : random.randrange(3, 15),
    }
    return render(request, 'management/users.html', content)

def applicationsPageView(request) :
    return render(request, 'management/applications.html')

def dianaPageView(request):
    content = {
        "name" : "Diana Warner",
        "email" : "alicia.r.coffey@trashymail.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_ai, skill_android, skill_bootstrap",
        "job" : "Medical Recepcionist",
    }
    return render(request, 'management/applicantredirect.html', content)

def tracyPageView(request):
    content = {
        "name" : "Tracy Wyman",
        "email" : "karine.f.bello@mailinator.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_design, skill_desk, skill_learning",
        "job" : "Clinical Research Associate",
    }
    return render(request, 'management/applicantredirect.html', content)

def timmyPageView(request):
    content = {
        "name" : "Timmy Schmidt",
        "email" : "bradley.g.chase@dodgit.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_debugging, skill_electronics, skill_engineering",
        "job" : "Territory Sales Representative	",
    }
    return render(request, 'management/applicantredirect.html', content)

def stevePageView(request):
    content = {
        "name" : "Steve Lewis",
        "email" : "dana.b.narcisse@trashymail.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_hadoop, skill_bootstrap, skill_go",
        "job" : "Bus Driver",
    }
    return render(request, 'management/applicantredirect.html', content)

def richardPageView(request):
    content = {
        "name" : "Richard Clark",
        "email" : "joanne.m.norton@mailinator.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_foundation, skill_consulting, skill_hardware",
        "job" : "Foreign Service Officer",
    }
    return render(request, 'management/applicantredirect.html', content)

def warrenPageView(request):
    content = {
        "name" : "Warren Cromar",
        "email" : "bernice.c.knott@pookmail.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_iphone, skill_android, skill_mobile",
        "job" : "Sales Analyst",
    }
    return render(request, 'management/applicantredirect.html', content)

def patriciaPageView(request):
    content = {
        "name" : "Patricia Bell",
        "email" : "gregory.d.chapman@trashymail.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_jsp, skill_http, skill_internet",
        "job" : "Medical Recepcionist",
    }
    return render(request, 'management/applicantredirect.html', content)

def larryPageView(request):
    content = {
        "name" : "Larry Deskins",
        "email" : "robert.b.wright@pookmail.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_ai, skill_android, skill_bootstrap",
        "job" : "Foreign Service Officer",
    }
    return render(request, 'management/applicantredirect.html', content)

def marshaPageView(request):
    content = {
        "name" : "Marsha Archer",
        "email" : "stephen.o.sweet@trashymail.com",
        "phone" : "(801) 422 - 5555",
        "skills" : "skill_maven, skill_modeling, skill_pascal",
        "job" : "Sales Analyst",
    }
    return render(request, 'management/applicantredirect.html', content)
