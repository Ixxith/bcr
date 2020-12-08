from django.urls import path
from .views import applyPageView, myapplicationsPageView, profilePageView, editprofilePageView

urlpatterns = [
    path("profile/", profilePageView, name="profile"),   
    path("editprofile/", editprofilePageView, name="editprofile/"), 
    path("apply/<int:jpid>/", applyPageView, name="apply/"),    
    path("applications/", myapplicationsPageView, name="applications/"),    
   
] 