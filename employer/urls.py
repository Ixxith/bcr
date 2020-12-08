from django.urls import path
from .views import profilePageView, editprofilePageView, myapplicationsPageView, newjpPageView, mypostingsPageView, editjpPageView, myapplicationsPageView

# Url patterns for manage template, job template, people template, and POST url patterns 

urlpatterns = [
    # Urls for pages 
    path("profile/", profilePageView, name="profile"),   
    path("editprofile/", editprofilePageView, name="editprofile/"),   
    path("postings/", mypostingsPageView, name="postings/"),   
    path("newjobposting/", newjpPageView, name="newjobposting/"),   
    path("editjobposting/<int:jpid>/", editjpPageView, name="editjobposting/"),
    path("applications/", myapplicationsPageView, name="jobapplications/"), 
] 