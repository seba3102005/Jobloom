from django import forms
from .models import MyAppliedJobs


class applyForm(forms.ModelForm):
    class Meta:
        model = MyAppliedJobs
        fields = ['cover_letter','salaryWithout','salaryWithFees','rate_increase',"increase_percentage"]
        widgets = {
            'cover_letter': forms.Textarea(attrs = {'id':'message','placeholder':'Type Here......','style':'background-color: transparent; border:1px solid white;'}),
            'rate_increase':forms.Select(attrs = {'id':'frequency',}),
            'salaryWithout' : forms.NumberInput(attrs = {'id':'salaryWithout','placeholder':"$7.2",'class':'hourly_rate'}),
            'salaryWithFees' : forms.NumberInput(attrs = {'id':'salaryWithFees','placeholder':"$7.2",'readonly':True,'class':'input_filed'}),
            'increase_percentage': forms.Select(attrs={'id':'increase'}),
            }
