from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

# View for about page template

def aboutPageView(request) :
    return render(request, 'applicationpages/about.html') 


# View for the index page

def indexPageView(request) :
    # sOutput = '<html><head><title>Main Page</title></head><body><p>This is the index page' + menu +'</body></html>'
    # return HttpResponse(sOutput) 
    
   return render(request, 'homepage/index.html') 




