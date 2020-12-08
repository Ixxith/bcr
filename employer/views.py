from django.shortcuts import render
from django.http import HttpResponseRedirect
from mainpages.models import Company, JobPosting, Newsletter, Person
from mainpages.forms import SkillForm, NewsLetterForm, AdministratorForm, EmployerForm, ApplicantForm, ZipForm, AddressForm, CompanyForm, JobPostingForm
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.db.models import Count

#from mainpages.models import Zip, Job, Paint, CompanyContact, Company, Employee
def authUser(request) :
    user = request.user
    if user.groups.filter(name='employer').exists():
        return True
    else:
        return False

def newjpPageView(request) :

    if request.POST:
        newjp = JobPosting()
        newjp.company = request.user.person.employer.company
        form = JobPostingForm(request.POST, instance=newjp)
        
       
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return HttpResponseRedirect('/employer/postings/')
    
    
    form = JobPostingForm()
    
    context = {
        'form': form,
        'authenticated' : authUser(request)
    }
    # Render page with context
    return render(request, 'employerpages/newjobposting.html', context) 

def editjpPageView(request, jpid) :

    if request.POST:
        jobpost = JobPosting.objects.get(pk=jpid)
        form = JobPostingForm(request.POST, instance=jobpost)
       
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/employer/postings/')
    
    jobpost = JobPosting.objects.get(pk=jpid)
    context = { 'authenticated' : False }
    
    if jobpost.company == request.user.person.employer.company:
    
        form = JobPostingForm(instance=jobpost)
    
        context = {
            'form': form,
            'jpid' : jpid,
            'authenticated' : authUser(request)
        }
   
       
        
    # Render page with context
    return render(request, 'employerpages/editjobposting.html', context) 


def editprofilePageView(request) :

    if request.POST:
        form = EmployerForm(request.POST, instance=request.user.person.employer)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/employer/profile/')
    
    
    empform = EmployerForm(instance=request.user.person.employer)
    
    context = {
        'form': empform,
        'authenticated' : authUser(request)
    }
    # Render page with context
    return render(request, 'employerpages/editprofile.html', context) 

def myapplicationsPageView(request) :

    
    
    
    context = {
      'authenticated' : authUser(request),
      'postings' : JobPosting.objects.filter(company=request.user.person.employer.company)
    }
    
    # Render page with context
    return render(request, 'employerpages/myapplications.html', context) 

def mypostingsPageView(request) :

    if request.POST:
        jp = JobPosting.objects.get(pk=request.POST.get('jpid'))
        jp.delete()
    
    jps = JobPosting.objects.filter(company=request.user.person.employer.company)
  
    context = {
      'authenticated' : authUser(request),
      'postings' : jps.annotate(applicationcount=Count('application'))
    }
    
    
    # Render page with context
    return render(request, 'employerpages/myjobpostings.html', context) 




def profilePageView(request) :

    
    
    
    context = {
      'authenticated' : authUser(request)
    }
    # Render page with context
    return render(request, 'employerpages/profile.html', context) 

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
