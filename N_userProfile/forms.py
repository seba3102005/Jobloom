from django import forms
from .models import Education,Skills,Languages,WorkExperience,project,Certification


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution','graduation_year']
        widget = {
            
            'institution': forms.TextInput(attrs = {'id':"institution",'placeholder':'City, Country','required':True}),
            'graduation_year': forms.TextInput(attrs  ={'id':"graduation_year",'placeholder':'EX:2027','required':True}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['name']
        widget = {
            'name': forms.TextInput(attrs = {'id':"name",'placeholder':'skate ,traveling ...','required':True}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name','organization','year']
        widget = {
            
            'name': forms.TextInput(attrs = {'id':"name",'placeholder':"Bachelor's degree",'required':True}),
            'organization': forms.TextInput(attrs  ={'id':"organization",'placeholder':'Faculty of Computers and Artificial Intelligence','required':True}),
            'year': forms.TextInput(attrs  ={'id':"year",'placeholder':'EX:2027','required':True}),
       
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = ['name']
        widget = {
            'name': forms.TextInput(attrs = {'id':"name",'placeholder':'German..','required':True}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ['name','image']
        widget = {
            'name': forms.TextInput(attrs = {'id':"name",'placeholder':'JobLoom','required':True}),
            'image': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your image URL','required' : True})
        }

class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['name','description']
        widget = {
            'name': forms.TextInput(attrs = {'id':"name",'placeholder':'Backend Developer','required':True}),
            'description': forms.TextInput(attrs  ={'id':"description",'description':'','required':True}),
        }





