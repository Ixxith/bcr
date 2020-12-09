from django.contrib import admin
#from .models import Job, Zip, Employee, Paint, Company, CompanyContact
from mainpages.models import Resume, Applicant
# Register your models here.

admin.site.register(Resume)
admin.site.register(Applicant)
