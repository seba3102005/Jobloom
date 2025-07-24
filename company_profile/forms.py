from django import forms
from .models import Employee,Job


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','position','image']
        widget = {
            
            'name': forms.TextInput(attrs = {'id':"name",'placeholder':'Enter your name','required':True}),
            'position': forms.TextInput(attrs  ={'id':"position",'placeholder':"Enter the Employee's position",'required':True}),
            'image': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter image URL','required' : True})
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name','description','image']
        widget = {
            
            'name': forms.TextInput(attrs = {'id':"name",'placeholder':'Enter your name','required':True}),
            'description': forms.TextInput(attrs  ={'id':"description",'placeholder':'Enter the job description','required':True}),
            'image': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter image URL','required' : True})
        }




