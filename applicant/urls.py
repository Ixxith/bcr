from django.urls import path
from .views import hirePageView

urlpatterns = [
    # Find the hire page
    path("", hirePageView, name="hire"),    
    # View for creating a new job from the hire page
   
] 