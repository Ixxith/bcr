from django.shortcuts import render

# Create your views here.
def newsletterPageView(request) :

    return render(request, 'management/newsletter.html')