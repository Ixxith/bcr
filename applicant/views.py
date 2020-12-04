from django.shortcuts import render
# from mainpages.models import Zip, Job, Paint, CompanyContact
from django.http import HttpResponseRedirect

# Create your views here.
def hirePageView(request) :
     
    
   # Get the locations and paints and add to the conext
    context = {
       
    }
    return render(request, 'applicationpages/hire.html', context)


