from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newsletterPageView(request) :
    return render(request, 'management/newsletter.html')

def showsendPageView(request):
    return render(request, 'management/newsletterredirect.html')