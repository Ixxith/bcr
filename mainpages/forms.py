from django import forms
from .models import Skill, Newsletter, Administrator, Employer, Applicant, Zip, Address, Company, JobPosting, JobCategory, Application, AutoApply, Resume 

stateChoices = (("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming"))


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
        

usertypes = (("Applicant","Applicant"),("Employer","Employer"))


from allauth.socialaccount.forms import SignupForm
class UserSelectionSignupForm(SignupForm):
    class Meta:
        fields = ['username']
        widgets = {
            'username' : forms.TextInput( attrs={'class' : 'form-control'}),
        }
      
    
    typeselection = forms.RadioSelect(attrs={'class' : 'form-control'}, choices=usertypes) 

    def signup(self, request, user):
        
        user.save()