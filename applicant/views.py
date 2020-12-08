from django.shortcuts import render
# from mainpages.models import Zip, Job, Paint, CompanyContact
from django.http import HttpResponseRedirect
from mainpages.models import JobPosting, Application, Applicant
from mainpages.forms import ApplicationForm, ApplicantForm
from datetime import datetime

def authUser(request) :
    user = request.user
    if user.groups.filter(name='applicant').exists():
        return True
    else:
        return False
     

# Create your views here.

def profilePageView(request) : 
   context = {
   'authenticated' : authUser(request)
   }
   # Render page with context
   return render(request, 'applicantpages/profile.html', context) 

def editprofilePageView(request) :

    if request.POST:
        form = ApplicantForm(request.POST, instance=request.user.person.applicant)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/applicant/profile/')
    
    
    form = ApplicantForm(instance=request.user.person.applicant)
    
    context = {
        'form': form,
        'authenticated' : authUser(request)
    }
    # Render page with context
    return render(request, 'applicantpages/editprofile.html', context) 

def myapplicationsPageView(request) :

   if request.POST:
      jp = Application.objects.get(pk=request.POST.get('jpid'))
      if jp.applicant == request.user.person.applicant:
         jp.delete()
      
   context = {
   'authenticated' : authUser(request),
   'applications' : Application.objects.filter(applicant=request.user.person.applicant)
   }

   # Render page with context
   return render(request, 'applicantpages/myapps.html', context) 


def applyPageView(request, jpid) :
   if request.POST:
      jobpost = JobPosting.objects.get(pk=jpid)
      app = Application()
      app.applicant = request.user.person.applicant
      app.jobposting = jobpost
      app.submitdate = datetime.now()
      app.status = 'Pending'
      
      form = ApplicationForm(request.POST, instance=app)
      
      if form.is_valid():
         form.save()
      return HttpResponseRedirect('/applicant/applications/')
   
   jobpost = JobPosting.objects.get(pk=jpid)
   context = { 'authenticated' : False }
   
   if jobpost.ispublic == True:
   
      form = ApplicationForm()
   
      context = {
         'form': form,
         'jpid' : jpid,
         'authenticated' : authUser(request)
      }
   
       
        
    # Render page with context
   return render(request, 'applicantpages/apply.html', context) 
