from django.db import models

# Create your models here.

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
    username = models.CharField(max_length=50)
    location = models.ForeignKey(Address, on_delete=models.DO_NOTHING)  
    
    @property
    def full_name(self):
        return '%s %s' % (self.firstname, self.lastname)
    
    def __str__(self):
                return (self.full_name)  


class Administrator(Person):
    role = models.CharField(max_length=50, blank=False, null=False)
    
class Applicant(Person):
    recievenewsletter = models.BooleanField(blank=False, null=False) 
    mentor = models.ForeignKey('self', on_delete=models.DO_NOTHING) 
    skills = models.ManyToManyField(Skill) 

class JobCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    gpaceiling = models.DecimalField(max_digits=3, decimal_places=2, blank=False, null=False) 

class Resume(models.Model):
    file = models.CharField(max_length=200, blank=False, null=False)
    applicant = models.ForeignKey(Applicant,  on_delete=models.DO_NOTHING) 
    
class AutoApply(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.DO_NOTHING)
    resume = models.ForeignKey(Resume, on_delete=models.DO_NOTHING)  
    wagerequirement = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)  
    needsrelocatassist = models.IntegerField(blank=False, null=False)  
    category = models.ManyToManyField(JobCategory)


class Company(models.Model):
    companyname = models.CharField(max_length=50, blank=False, null=False) 
    location = models.ForeignKey(Address,  on_delete=models.DO_NOTHING) 

class Employer(Person):
    position = models.CharField(max_length=50, blank=False, null=False)
    supervisor = models.ForeignKey('self',  on_delete=models.DO_NOTHING) 
    company = models.ForeignKey(Company,  on_delete=models.DO_NOTHING) 

class JobPosting(models.Model):
    company = models.ForeignKey(Company,  on_delete=models.DO_NOTHING) 
    category = models.ManyToManyField(JobCategory) 
    requiredskills = models.ManyToManyField(Skill) 
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=5000, blank=False, null=False)
    zipcode = models.ForeignKey(Zip,  on_delete=models.DO_NOTHING) 
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
    jobposting = models.ForeignKey(JobPosting, on_delete=models.DO_NOTHING)
    submitdate = models.DateTimeField(blank=False, null=False)  
    status = models.CharField(max_length=50, blank=False, null=False)
    autoapply = models.ForeignKey(AutoApply, on_delete=models.DO_NOTHING)
    resume = models.ForeignKey(Resume, on_delete=models.DO_NOTHING)
    applicant = models.ForeignKey(Applicant, on_delete=models.DO_NOTHING)

class ContactInformation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING) 
    contacttype = models.CharField(max_length=20, blank=False, null=False)
    value = models.CharField(max_length=30, blank=False, null=False)
    ispublic = models.BooleanField(blank=False, null=False) 

class Newsletter(models.Model):
    subject = models.CharField(max_length=100, blank=False, null=False)
    body = models.CharField(max_length=100000, blank=False, null=False)
    sentdate = models.DateTimeField(blank=False, null=False)  
    sentto = models.ManyToManyField(Person, related_name='sentto')
    sentby = models.ForeignKey(Administrator,  on_delete=models.DO_NOTHING,related_name='sentby') 


def updateObjectFromForm(Object, form):
    allfieldsFilled = True
    fields = Object._meta.fields
    assocations = []
    for f in fields:
        if f.name != 'id': # Don't edit ids
            if form.get(f.Name) != None:
                if f.many_to_many:
                    # Many to many
                    assocations.append(f)
                elif f.many_to_one:
                    # Foreign Key
                    assocations.append(f)
                else:
                    # Normal attribute
                    Object[f.name] = form.get(f.name)
            else:
                # Not in form, therefore this form did not have all the data
                allfieldsFilled = False
    
    Object.save()
    
    for f in assocations:
        if f.name != 'id': # Don't edit ids
            if form.get(f.Name) != None:
                if f.many_to_many:
                    # Many to many
                    Object[f.name].clear()
                    for oid in form.get(f.name):
                        Object[f.name].add(f.related_model.objects.get(pk=oid))
                else:
                    # Foreign Key
                    Object[f.name] = f.related_model.objects.get(pk=form.get(f.name))
            else:
                # Not in form, therefore this form did not have all the data
                allfieldsFilled = False
    return allfieldsFilled
