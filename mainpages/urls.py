from django.urls import path, include
from .views import indexPageView, aboutPageView, signupPageView
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView
from allauth.socialaccount.views import SignupView
from mainpages.forms import UserSelectionSignupForm
import datetime
class MySignupView(SignupView):
    form = UserSelectionSignupForm
    template_name = 'signup.html'
    
# Urls for the main page and the about page

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about", aboutPageView, name="about"), 
    url(r'^accounts/social/signup', MySignupView.as_view(), name='socialaccount_signup'),
    
    url(r'^logout/$', LogoutView.as_view(), {'next_page': ''}, name='logout'),
    
    
] 