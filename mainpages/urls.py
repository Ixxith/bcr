from django.urls import path
from .views import indexPageView
from .views import aboutPageView

# Urls for the main page and the about page

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about", aboutPageView, name="about"),    
  
] 