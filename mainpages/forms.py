from django import forms
from .models import Skill, Newsletter, Administrator, Employer, Applicant, Zip, Address, Company, JobPosting, JobCategory, Application, AutoApply, Resume 

stateChoices = (("AL","Alabama"),	("AK","Alaska"),	("AZ","Arizona"),	("AR","Arkansas"),	("CA","California"),	("CO","Colorado"),	("CT","Connecticut"),	("DE","Delaware"),	("FL","Florida"),	("GA","Georgia"),	("HI","Hawaii"),	("ID","Idaho"),	("IL","Illinois"),	("IN","Indiana"),	("IA","Iowa"),	("KS","Kansas"),	("KY","Kentucky"),	("LA","Louisiana"),	("ME","Maine"),	("MD","Maryland"),	("MA","Massachusetts"),	("MI","Michigan"),	("MN","Minnesota"),	("MS","Mississippi"),	("MO","Missouri"),	("MT","Montana"),	("NE","Nebraska"),	("NV","Nevada"),	("NH","New Hampshire"),	("NJ","New Jersey"),	("NM","New Mexico"),	("NY","New York"),	("NC","North Carolina"),	("ND","North Dakota"),	("OH","Ohio"),	("OK","Oklahoma"),	("OR","Oregon"),	("PA","Pennsylvania"),	("RI","Rhode Island"),	("SC","South Carolina"),	("SD","South Dakota"),	("TN","Tennessee"),	("TX","Texas"),	("UT","Utah"),	("VT","Vermont"),	("VA","Virginia"),	("WA","Washington"),	("WV","West Virginia"),	("WI","Wisconsin"),	("WY","Wyoming"))


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name"]
        widgets = {
            'name' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input skill name'})
        }
        labels = {
        "name": "Skill Name"
    }
        
class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ["name"]
        widgets = {
            'name' : forms.TextInput( attrs={'class' : 'form-control'})
        }
        labels = {
        "name": "Job Category Name"
    }
        
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["subject", "body", "sentto"]
        widgets = {
            'subject' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input newsletter subject'}),
            'body' : forms.Textarea( attrs={'class' : 'form-control', 'placeholder': 'Input newsletter body here'}),
            'sentto' : forms.SelectMultiple( attrs={'class' : 'form-control'})
        }
        
        labels = { 'sentto' : "Choose senders"}
        
class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ["username","role", "firstname", "lastname", "birthdate", 'location']
        widgets = {
            'username' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input subject'}),
            'role' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input role'}),
            'firstname' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input first name'}),
            'lastname' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input last name'}),
            'birthdate' : forms.DateInput( attrs={'class' : 'form-control', 'placeholder': 'mm/dd/yyyy', 'format' : 'mm/dd/yyyy'}),
            
        }
        
        labels = { 'firstname' : "First Name",
                  'lastname' : "Last Name",
                  'birthdate' : "Birth Date"}
            
        
        
class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ["username","position", "firstname", "lastname", "birthdate", 'location', 'company']
        widgets = {
            'username' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input subject'}),
            'position' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input role'}),
            'firstname' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input first name'}),
            'lastname' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input last name'}),
            'birthdate' : forms.DateInput( attrs={'class' : 'form-control', 'placeholder': 'mm/dd/yyyy', 'format' : 'mm/dd/yyyy'}),
            'location' : forms.Select( attrs={'class' : 'form-control'}),
            'company' : forms.Select( attrs={'class' : 'form-control'})
        }
        
        labels = { 'firstname' : "First Name",
                  'lastname' : "Last Name",
                  'birthdate' : "Birth Date"}
        
class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ["username", "firstname", "lastname", "birthdate", 'location','recievenewsletter']
        widgets = {
            'username' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input subject'}),
            'position' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input role'}),
            'firstname' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input first name'}),
            'lastname' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input last name'}),
            'birthdate' : forms.DateInput( attrs={'class' : 'form-control', 'placeholder': 'mm/dd/yyyy', 'format' : 'mm/dd/yyyy'}),
            'location' : forms.Select( attrs={'class' : 'form-control'}),
            'recievenewsletter' : forms.CheckboxInput(attrs={'class' : 'checkbox'}),
        }
        
        labels = { 'firstname' : "First Name",
                  'lastname' : "Last Name",
                  'birthdate' : "Birth Date",
                  'recievenewsletter' : 'Would you like to recieve a newsletter with potential job offers?'}
        

class ZipForm(forms.ModelForm):
    class Meta:
        model = Zip
        fields = ["code", "city", "state"]
        widgets = {
            'code' : forms.NumberInput( attrs={'class' : 'form-control', 'min': '10000', 'max': '99999', 'placeholder': 'Input Zip Code'}),
            'city' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input city'}),
            'state' : forms.Select( attrs={'class' : 'form-control'}, choices = stateChoices),
        }
        
        labels = { 'code' : "Zip Code"
                  }
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["addressline1", "addressline2", "zipcode"]
        widgets = {
            'addressline1' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input Address Line 1'}),
            'addressline2' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input Address Line 2'}),
            'zipcode' : forms.Select( attrs={'class' : 'form-control'}),
        }
        
        labels = {'addressline1' : "Address Line 1",
                    'addressline2' : "Address Line 2",
                    'zipcode' : "Zip Code",
                  }
        
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["companyname", 'location']
        widgets = {
            'companyname' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input Company Name'}),
            'location' : forms.Select( attrs={'class' : 'form-control'}),
        }
        
        labels = {'companyname' : "Company Name",
                   

                  }
        
                
class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ["title", "description", "pay", "wagetype", 'gpareq', 'relocationassist', 'appopendate', 'appclosingdate', 'decisiondate', 'jobstartdate', 'company', 'zipcode', 'requiredskills', 'category','ispublic']
        widgets = {
            'title' : forms.TextInput( attrs={'class' : 'form-control'}),
            'description' : forms.TextInput( attrs={'class' : 'form-control'}),
            'pay' : forms.NumberInput( attrs={'class' : 'form-control'}),
            'wagetype' : forms.TextInput( attrs={'class' : 'form-control'}),
            'gpareq' : forms.TextInput( attrs={'class' : 'form-control'}),
            'relocationassist' : forms.CheckboxInput(attrs={'class' : 'checkbox'}),
            'appopendate' : forms.DateInput( attrs={'class' : 'form-control', 'placeholder': 'mm/dd/yyyy', 'format' : 'mm/dd/yyyy'}),
            'appclosingdate' : forms.DateInput( attrs={'class' : 'form-control', 'placeholder': 'mm/dd/yyyy', 'format' : 'mm/dd/yyyy'}),
            'decisiondate' : forms.DateInput( attrs={'class' : 'form-control', 'placeholder': 'mm/dd/yyyy', 'format' : 'mm/dd/yyyy'}),
            'jobstartdate' : forms.DateInput( attrs={'class' : 'form-control', 'placeholder': 'mm/dd/yyyy', 'format' : 'mm/dd/yyyy'}),
            'company' : forms.Select( attrs={'class' : 'form-control'}),
            'zipcode' : forms.Select( attrs={'class' : 'form-control'}),
            'requiredskills' : forms.SelectMultiple( attrs={'class' : 'form-control'}),
            'category' : forms.SelectMultiple( attrs={'class' : 'form-control'}),
            'ispublic' : forms.CheckboxInput(attrs={'class' : 'checkbox'}),
        }
        
        labels = { 'wagetype' : "Wage Type",
                  'gpareq' : "GPA Requirement",
                  'relocationassist' : "Will relocation assistance be provided?",
                  'appopendate' : "Application Open Date",
                  'appclosingdate' : "Application Closing Date",
                  'decisiondate' : "Decision Date",
                  'jobstartdate' : 'Job Start Date',
                  'zipcode' : "Job Zip Code",
                  'requiredskills' : "Skills Required",
                  'category' : "Job Categories",
                  'ispublic' : "Publish Job?"}

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']
        widgets = {
            'resume' : forms.Select( attrs={'class' : 'form-control'}),
        }
        
class AutoApplyForm(forms.ModelForm):
    class Meta:
        model = AutoApply
        fields = ['wagerequirement', 'needsrelocatassist', 'category']
        widgets = {
            'wagerequirement' : forms.NumberInput( attrs={'class' : 'form-control'}), 
            'relocationassist' : forms.CheckboxInput(attrs={'class' : 'checkbox'}),
            'category' : forms.SelectMultiple( attrs={'class' : 'form-control'})
        }
        labels = {
            'wagerequirement' : "Wage Requirement",
            'needsrelocatassist' : "Only apply to jobs with relocation assistance?",
            'category' : 'Job categories'
        }
        
        
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
        widgets = {
            'file' : forms.TextInput( attrs={'class' : 'form-control'}),
        }
        

usertypes = (("applicant","Applicant"),("employer","Employer"),)

from allauth.socialaccount.forms import SignupForm
class UserSelectionSignupForm(SignupForm):
    
    skills = ((o.pk, o.name) for o in Skill.objects.all())
    companies = ((o.pk, o.companyname) for o in Company.objects.all())
    
    firstname = forms.CharField(label='First name', max_length=100) 
    lastname = forms.CharField(label='Last name', max_length=100) 
    addressline1 = forms.CharField(label='Address Line 1', max_length=100) 
    addressline2 = forms.CharField(label='Address Line 2', max_length=100) 
    city = forms.CharField(label='City', max_length=100) 
    state = forms.ChoiceField(widget=forms.Select(), choices=stateChoices, label="State")
    zipcode = forms.CharField(widget =forms.NumberInput(), label='Zip Code', max_length=5) 
    birthdate = forms.CharField(widget=forms.DateInput(format='yyyy-mm-dd'), label = 'Birth Date (yyyy-mm-dd)')
    persontype = forms.ChoiceField(widget=forms.RadioSelect(), choices=usertypes, label="Are you an applicant or an employer?")
    
    # Employer section
    employerrole = forms.CharField(label='Position', max_length=100, required=False) 
    employerselect = forms.ChoiceField(widget=forms.Select(), choices=companies, label="Choose your company or enter it's info below", required=False)
    employer = forms.CharField(label='Company', max_length=100, required=False) 
    employeraddressline1 = forms.CharField(label='Company Address Line 1', max_length=100, required=False) 
    employeraddressline2 = forms.CharField(label='Company Address Line 2', max_length=100, required=False) 
    employercity = forms.CharField(label='Company City', max_length=100, required=False)
    employerstate = forms.ChoiceField(widget=forms.Select(), choices=stateChoices, label="Company State", required=False)
    employerzipcode = forms.CharField(widget =forms.NumberInput(), label='Company Zip Code', max_length=5, required=False) 

    # Applicant Section
    
    
    
    
    apprecievenewsletter = forms.CharField(label="Would you like to recieve a newsletter?", widget=forms.CheckboxInput(), required=False)    
    #appcategories = forms.ChoiceField(widget=forms.SelectMultiple(), choices=JobCategory.objects.all(), label="Choose job categories you are interested in", required=False)
    appskills = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=skills, label="Choose skills you have", required=False)
    from django.utils.timezone import datetime

    def save(self, request):
       
        f = request.POST    
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        
        newPerson = None
        if f.get('persontype') == "employer":
            newPerson = Employer()
        else:
            newPerson = Applicant()
        newPerson.username = f.get('username')
        newPerson.firstname = f.get('firstname')
        newPerson.lastname = f.get('lastname')
        newPerson.birthdate = (f.get('birthdate') + " 00:01")
        pnewAddress = Address()
        pnewAddress.addressline1 = f.get('addressline1')
        pnewAddress.addressline2 = f.get('addressline2')
        pzipz = Zip.objects.filter(code= f.get('zipcode')) 
        if pzipz.count() == 0:
            pzipz = Zip()
            pzipz.code = f.get('zipcode')
            pzipz.city = f.get('city')
            pzipz.state = f.get('state')
            pzipz.save()
        else:
            pzipz = pzipz.first()
        pnewAddress.zipcode = pzipz
        pnewAddress.save()
        newPerson.location = pnewAddress
        
        if f.get('persontype') == "employer":
            
            newPerson.position = f.get('employerrole')
            companyquery = Company.objects.filter(pk = f.get('employerselect'))
            company = None
            if companyquery.count() == 0:
                company = Company()
                company.companyname = f.get('employer')
                newAddress = Address()
                newAddress.addressline1 = f.get('employeraddressline1')
                newAddress.addressline2 = f.get('employeraddressline2')
                zipz = Zip.objects.filter(code= f.get('employerzipcode')) 
                if zipz.count() == 0:
                    zipz = Zip()
                    zipz.code = f.get('employerzipcode')
                    zipz.city = f.get('employercity')
                    zipz.state = f.get('employerstate')
                    zipz.save()
                else:
                    zipz = zipz.first()
                newAddress.zipcode = zipz
                newAddress.save()
                company.location = newAddress
                company.save()
            else:
                company = companyquery.first()
            newPerson.company = company
            newPerson.save()
            
        else:
           
            if  f.get('apprecievenewsletter') == 'on':
                newPerson.recievenewsletter = True
            else:
                newPerson.recievenewsletter = False
            newPerson.save()
            #for jc in f.get('appcategories:
               # jcc = JobCategory.objects.get(pk = jc)
              #  if jcc:
               #     newPerson.category.add(jcc)
            for s in f.get('appskills'):
                sc = Skill.objects.get(pk = s)
                if sc:
                    newPerson.skills.add(sc)

        user = super(UserSelectionSignupForm, self).save(request)
        # Add your own processing here.
        
        newPerson.user = user
        newPerson.save()
        # You must return the original result.
        return user