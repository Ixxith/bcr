from django.urls import path

from .views import managePageView

# Url patterns for manage template, job template, people template, and POST url patterns 

urlpatterns = [
    # Urls for pages 
    path("manage/", managePageView, name="manage"),   
    
   
] 