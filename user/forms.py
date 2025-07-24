from django import forms
from .models import NormalUser,CompanyUser


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'id':"password", 'placeholder':"Enter your password", 'required':True}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={ 'id':"confirm-password", 'placeholder':"Confirm your password", 'required':True}))
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'id': 'email','placeholder': 'Enter your email','required': True }))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id': 'name','placeholder': 'Enter your full name','required': True }))
    phoneNo = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'id':'phone','placeholder':'Enter your phone number','required':True}))


    class Meta():
        model = NormalUser
        fields = ['gender']
        widgets = {
            'gender': forms.Select(attrs={
                'id': 'gender',
                'required': True
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError('password don\'t match ')
        return cleaned_data
    
class CompanyRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'id':"password", 'placeholder':"Enter your password", 'required':True}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={ 'id':"confirm-password", 'placeholder':"Confirm your password", 'required':True}))
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'id': 'company-email','placeholder': 'Enter a valid business email','required': True }))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id': 'company-name','placeholder': 'Enter your company name','required': True }))
    phoneNo = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'id':'phone','placeholder':'Enter company contact number','required':True}))

    class Meta:
        model = CompanyUser
        fields = ['industry','location','website']
        widgets = {
            'industry': forms.TextInput(attrs = {'id':'industry','placeholder':'e.g., IT, Finance, Healthcare','required':True}) ,
            'location': forms.TextInput(attrs = {'id':"location",'placeholder':'City, Country','required':True}),
            'website': forms.TextInput(attrs  ={'id':"website",'placeholder':'https://example.com','required':True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError('password don\'t match ')
        return cleaned_data
    
    # from user.models import CustomUser,CompanyUser
    # CustomUser.objects.all().delete()
    # CompanyUser.objects.all().delete()