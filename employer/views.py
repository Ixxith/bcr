from django.shortcuts import render
from django.http import HttpResponseRedirect
from mainpages.models import Company, JobPosting, Newsletter
from mainpages.forms import SkillForm, NewsLetterForm, AdministratorForm, EmployerForm, ApplicantForm, ZipForm, AddressForm, CompanyForm, JobPostingForm
from django.shortcuts import get_object_or_404

#from mainpages.models import Zip, Job, Paint, CompanyContact, Company, Employee
def authUser(request) :
    user = request.user
    if user.groups.filter(name='employer').exists():
        return True
    else:
        return False


def testPageView(request) :

   
    form = JobPostingForm()
    
    context = {
      'form' :  form,
      'authenticated' : authUser(request)
    }
    # Render page with context
    return render(request, 'employerpages/test.html', context) 

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
