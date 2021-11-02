from .models import Business
from django import forms

class BusinessForms(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Business
        fields= ['name','email','business_image','location']
class PostForms(forms.ModelForm):
    class Post:
        fields=['post']