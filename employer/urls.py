from django.urls import path

from .views import testPageView

# Url patterns for manage template, job template, people template, and POST url patterns 

urlpatterns = [
    # Urls for pages 
    path("test/", testPageView, name="test"),   
    
   
] 