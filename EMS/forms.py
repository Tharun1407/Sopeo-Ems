from django.core import validators 
from django import forms 
from .models import Employees 


class employeeForm(forms.ModelForm):
    
    
    class Meta:
        model = Employees 
        fields = ['Name','DOB','DOJ','Department','Post','Address','City','Country','Zipcode','State','Active']
        
        