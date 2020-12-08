from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NewsLetterForm

# Create your views here.
def newsletterPageView(request) :
    return render(request, 'management/newsletter.html')