from django import forms
from .models import  NewsletterForm
from django.contrib.auth.models import Group

class NewsLetterForm(forms.ModelForm):
    typetosendto = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices = newsletterchoices, label="Select the recievers of this message")
    class Meta:
        model = Newsletter
        fields = ["subject", "body", #"sentto"
                  ]
        widgets = {
            'subject' : forms.TextInput( attrs={'class' : 'form-control', 'placeholder': 'Input newsletter subject'}),
            'body' : forms.Textarea( attrs={'class' : 'form-control', 'placeholder': 'Input newsletter body here'}),
            #'sentto' : forms.SelectMultiple( attrs={'class' : 'form-control'})
        }