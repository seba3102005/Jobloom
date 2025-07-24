from django import forms
from .models import JobOffer,Skill


class JobForm(forms.ModelForm):
    
    new_skills = forms.CharField(
        required=True,
        label="Required Skills",
        help_text="Enter skills separated by commas.",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Python, Django, Machine Learning'})
    )
    

    class Meta:
        model = JobOffer
        fields = ['title', 'description', 'hourly_rate', 'experience','new_skills']
        


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']


