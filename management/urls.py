from django.urls import path
from .views import newsletterPageView, showsendPageView, usersPageView, applicationsPageView, dianaPageView, tracyPageView, timmyPageView, stevePageView, richardPageView, warrenPageView, patriciaPageView, larryPageView, marshaPageView
# Url patterns for manage template, job template, people template, and POST url patterns 

urlpatterns = [
    # Urls for pages
    path("users/", usersPageView, name="users"), 
    path("applications/", applicationsPageView, name="applications"),
    path("diana/", dianaPageView, name="diana"),
    path("newsletter/", newsletterPageView, name="newsletter"), 
    path("send/", showsendPageView, name="send"),
    path("tracy/", tracyPageView, name="tracy"),
    path("timmy/", timmyPageView, name="timmy"),
    path("steve/", stevePageView, name="steve"),
    path("richard/", richardPageView, name="richard"),
    path("warren/", warrenPageView, name="warren"),
    path("patricia/", patriciaPageView, name="patricia"),
    path("larry/", larryPageView, name="larry"),
    path("marsha/", marshaPageView, name="marsha"),
    
   
] 