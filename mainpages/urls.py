from django.urls import path, include
from .views import indexPageView, aboutPageView, jpPageView
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from allauth.socialaccount.views import SignupView
from mainpages.forms import UserSelectionSignupForm
class MySignupView(SignupView):
    form = UserSelectionSignupForm
    template_name = 'signup.html'
    
# Urls for the main page and the about page

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about", aboutPageView, name="about"), 
    path("jobpostings", jpPageView, name="/jobpostings"),
   # path("matchbox/", azure_matchbox, name="azure_job"),
    url(r'^accounts/social/signup', MySignupView.as_view(), name='socialaccount_signup'),
    
    url(r'^logout/$', LogoutView.as_view(), {'next_page': ''}, name='logout'),
    
    
] 