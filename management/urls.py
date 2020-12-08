from django.urls import path
from .views import newsletterPageView


# Url patterns for manage template, job template, people template, and POST url patterns 

urlpatterns = [
    # Urls for pages 
    path("newsletter/", newsletterPageView, name="newsletter"), 
    
   
] 