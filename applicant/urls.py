from django.urls import path
from .views import applyPageView, myapplicationsPageView, profilePageView, editprofilePageView, editresumePageView, newresumePageView

urlpatterns = [
    path("profile/", profilePageView, name="profile"),   
    path("editprofile/", editprofilePageView, name="editprofile/"), 
    path("apply/<int:jpid>/", applyPageView, name="apply/"),    
    path("applications/", myapplicationsPageView, name="applications/"),    
    path("editresume/<int:rid>/", editresumePageView, name="editresume/"),    
    path("newresume/", newresumePageView, name="newresume/"),    
] 