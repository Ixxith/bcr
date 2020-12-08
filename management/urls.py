from django.urls import path
from .views import newsletterPageView
from .views import showsendPageView


# Url patterns for manage template, job template, people template, and POST url patterns 

urlpatterns = [
    # Urls for pages 
    path("newsletter/", newsletterPageView, name="newsletter"), 
    path("send/", showsendPageView, name="send"),
    
   
] 