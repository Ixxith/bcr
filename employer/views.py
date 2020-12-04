from django.shortcuts import render
from django.http import HttpResponseRedirect
#from mainpages.models import Zip, Job, Paint, CompanyContact, Company, Employee


# Function for the manage page view
def managePageView(request) :
    # Get objects for displaying data
 
    context = {
        
    }
    # Render page with context
    return render(request, 'applicationpages/manage.html', context) 
   

# Function for a specific page
def jobPageView(request, job_id) :
   
    context = {
     
    }
    
    return render(request, 'applicationpages/job.html', context)   

# Pass the model objects to the manage page
