from django.shortcuts import render
# from mainpages.models import Zip, Job, Paint, CompanyContact
from django.http import HttpResponseRedirect
from mainpages.models import JobPosting, Application, Applicant, Resume, Skill, ApplicantSkills
from mainpages.forms import ApplicationForm, ApplicantForm, ResumeForm
from datetime import datetime

def authUser(request) :
    user = request.user
    if user.groups.filter(name='applicant').exists():
        return True
    else:
        return False
     

# Create your views here.

import json
import numpy as np

def azure_regression(applicant) :
    
    import urllib 
    skillListColumns = ["user_id", "status", "city", "job_title", "organization_id", "contracts", "matching_skills"]
    skillListValues = ['0','none', 'none', 'none', '0', 'none', '1']
    skillstoSearchFor = ["ai",	"ajax",	"analytical",	"analytics",	"android",	"angular",	"artificial neural network",	"asp.net",	"assembleur",	"assembly",	"attention to detail",	"backend",	"big data",	"bootstrap",	"certifications",	"cloud computing",	"coaching",	"coding",	"collaboration",	"communication",	"communication technologies",	"consulting",	"content marketing",	"control systems",	"critical thinking",	"customer service",	"data analysis",	"data analytics",	"data collection",	"data management",	"data mining",	"data processing",	"databases",	"debugging",	"deep learning",	"design",	"design patterns",	"designer",	"desk",	"diagnostics",	"digital marketing",	"documentation",	"dom",	"dos",	"e-commerce",	"eclipse",	"electronics",	"engineering",	"ensemble",	"extjs",	"fortran",	"foundation",	"framework",	"frontend",	"git",	"go",	"graphic design",	"hadoop",	"hardware",	"hive",	"html",	"http",	"implementation",	"innovation",	"insights",	"internet",	"iphone",	"iptables",	"javascript",	"jquery",	"jsp",	"leadership",	"less",	"linux",	"lte",	"machine learning",	"mathematics",	"matlab",	"maven",	"mentoring",	"mobile",	"modeling",	"multitasking",	"network security",	"networks",	"node.js",	"nodejs",	"operating system",	"organizational",	"pascal",	"penetration testing",	"phonegap",	"php",	"postfix",	"powershell",	"presentation",	"prestashop",	"priorities",	"problem solving",	"processing",	"programming",	"project management",	"project manager",	"prototyping",	"python",	"renewable energy",	"reporting",	"reporting tools",	"sas",	"scrum",	"sencha touch",	"shiny",	"social media marketing",	"software development",	"solution development",	"spark",	"sql",	"sql server",	"statistical analysis",	"svg",	"swing",	"tableau",	"teamwork",	"tech support",	"technical",	"telecom",	"time management",	"training",	"troubleshooting",	"vb.net",	"visio",	"volleyball",	"web analytics",	"web development",	"web services",	"website development",	"wimax",	"windows",	"word",	"wordpress"]

    
    
    for skill in skillstoSearchFor:
        skillListColumns.append('skill_'+skill)
        skquery = Skill.objects.filter(name=skill)
        valuetoappend = '0'
        
        if skquery.count() > 0:
            skill = skquery.first()
            asquery = ApplicantSkills.objects.filter(applicant=applicant, skill=skill)
            if asquery.count() > 0:
                valuetoappend = "5"
        
        skillListValues.append(valuetoappend)
            
    

    data = {
            "Inputs": {
                    "input1": {
                        "ColumnNames": skillListColumns,
                        "Values": [skillListValues]
                            }
                    }
            }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/15d3874116954e749dcf8db99722f4a4/services/b56e1e30902c4b549a3e9623f88e9ff6/execute?api-version=2.0&details=true'
    api_key = 'RGo8VxaINEAVx2c81xiIjjTwOgGt5ZrHeF6+Mq/v0HLPCT/eTxlkWah4hXy7pR4se6fF47w8gpXOWQc6AQ7n6Q==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req)
    result = response.read()
    
    result = json.loads(result) # Convert JSON byte stream into dictionary
    #breakpoint()
    prediction = (float(result['Results']['output1']['value']['Values'][0][27]) / 1.8) * 100
    if prediction > 100:
        prediction = 100
    return round(prediction)

import math

def profilePageView(request) : 
    if request.POST:
        resume = Resume.objects.get(pk=request.POST.get("rid"))
        if resume.applicant == request.user.person.applicant:
            resume.delete()
        return HttpResponseRedirect('/applicant/profile/')

    hirabilityscore = azure_regression(request.user.person.applicant)
    if hirabilityscore is None:
        hirabilityscore = 0

    calenderrender = []
    
    
    for job in  JobPosting.objects.all():
        if job.appopendate.month == 12:
            day = job.appopendate.day
            calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Open Date'})
        if job.appclosingdate.month == 12:
            day = job.appclosingdate.day
            calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Closing Date'})
        if job.jobstartdate.month == 12:
            day = job.jobstartdate.day
            calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Open Date'})
        if job.decisiondate.month == 12:
            day = job.decisiondate.day
            calenderrender.append({'row' : math.floor(day/7)+2, 'col' : (day % 7)+2, 'text' : job.title + ' - Application Decision Date'})


    context = {
    'authenticated' : authUser(request),
    'resumes' : Resume.objects.filter(applicant=request.user.person.applicant),
    'hirability' : hirabilityscore,
    'calenderobjects' : calenderrender
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


def newresumePageView(request) :

    if request.POST:
        resume = Resume()
        resume.applicant = request.user.person.applicant
        form = ResumeForm(request.POST, files = request.FILES, instance=resume)
        
       
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return HttpResponseRedirect('/applicant/profile/')
    
    
    form = ResumeForm()
    
    context = {
        'form': form,
        'authenticated' : authUser(request)
    }
    # Render page with context
    return render(request, 'applicantpages/newresume.html', context) 

def editresumePageView(request, rid) :

    if request.POST:
        resume = Resume.objects.get(pk=rid)
        form = ResumeForm(request.POST, request.FILES, instance=resume)
       
        if form.is_valid() and resume.applicant == request.user.person.applicant:
            form.save()
        return HttpResponseRedirect('/applicant/profile/')
    
    resume = Resume.objects.get(pk=rid)
    context = { 'authenticated' : False }
    
    if resume.applicant == request.user.person.applicant:
        
        form = ResumeForm(instance=resume)

        context = {
            'form': form,
            'rid' : rid,
            'authenticated' : authUser(request)
        }
   
       
        
    # Render page with context
    return render(request, 'applicantpages/editresume.html', context) 


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
