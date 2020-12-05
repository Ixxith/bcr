from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Zip(models.Model):
    code = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)

class Address(models.Model):
    addressline1 = models.CharField(max_length=50, blank=False, null=False)  
    addressline2 = models.CharField(max_length=50, blank=False, null=False) 
    zipcode = models.ForeignKey(Zip, on_delete=models.DO_NOTHING)
 

class Skill(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)


class Person(models.Model):
    firstname = models.CharField(max_length=50, blank=False, null=False)  
    lastname = models.CharField(max_length=50, blank=False, null=False)  
    birthdate = models.DateTimeField(blank=False, null=False)  
    location = models.ForeignKey(Address, on_delete=models.DO_NOTHING)  

class Administrator(Person):
    role = models.CharField(max_length=50, blank=False, null=False)
class Applicant(Person):
    recievenewsletter = models.BooleanField(blank=False, null=False) 
    mentor = models.ForeignKey(Person, on_delete=models.DO_NOTHING) 
    autoapply = models.BooleanField(blank=False, null=False)  .
    wagerequirement = models.IntegerField(blank=False, null=False)  
    needsrelocatassist = models.BooleanField(blank=False, null=False)  
    skills = models.ManyToManyField(Skill) 

class JobCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    gpaceiling = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False) 

class Autoapply(models.Model):
    applicant = models.ForeignKey(Person, on_delete=models.DO_NOTHING)  
    wagerequirement = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)  
    needsrelocatassist = models.IntegerField(blank=False, null=False)  
    category = models.ManyToManyField(JobCategory)


class Company(models.Model):
    companyname = models.CharField(max_length=50, blank=False, null=False) 
    location = models.ForeignKey(Address,  on_delete=models.DO_NOTHING) 

class Employer(Person):
    position = models.CharField(max_length=50, blank=False, null=False)
    supervisor =models.ForeignKey(Employer,  on_delete=models.DO_NOTHING) 
    company = models.ForeignKey(Company,  on_delete=models.DO_NOTHING) 

class JobPosting(models.Model):
    company = models.ForeignKey(Address,  on_delete=models.DO_NOTHING) 
    category = models.ManyToManyField(JobCategory) 
    requiredskills = models.ManyToManyField(Skill) 
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=5000, blank=False, null=False)
    zip = models.ForeignKey(Zip,  on_delete=models.DO_NOTHING) 
    pay = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    wagetype = models.CharField(max_length=50, blank=False, null=False) 
    gpareq = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False)
    ispublic = models.BooleanField(blank=False, null=False)
    relocationassist = models.BooleanField(blank=False, null=False)
    appopendate = models.DateTimeField(blank=False, null=False) 
    appclosingdate = models.DateTimeField(blank=False, null=False)
    decisiondate = models.DateTimeField(blank=False, null=False)  
    jobstartdate = models.DateTimeField(blank=False, null=False)  

class Application(models.Model):
    jobposting = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    submitdate = models.DateTimeField(blank=False, null=False)  
    status = models.CharField(blank=False, null=False)
    autoapply = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    resume = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    applicant = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

class ContactInformation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING) 
    contacttype = models.CharField(max_length=20, blank=False, null=False)
    value = models.CharField(max_length=30, blank=False, null=False)
    ispublic = models.BooleanField(blank=False, null=False) 

class Newsletter(models.Model):
    subject = models.CharField(max_length=100, blank=False, null=False)
    body = models.CharField(max_length=100000, blank=False, null=False)
    sentdate = models.DateTimeField(blank=False, null=False)  
    sentto = models.ManyToManyField(Person)
    sentby = models.ForeignKey(Person,  on_delete=models.DO_NOTHING) 
class Resume(models.Model):
    file = models.CharField(max_length=200, blank=False, null=False)
    applicant = models.ForeignKey(Applicant,  on_delete=models.DO_NOTHING) 





   