from django.shortcuts import render,redirect
from .forms import UserRegisterForm,CompanyRegisterForm
from .models import CustomUser,NormalUser,CompanyUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request,'index.html')




@login_required(login_url='login')
def job_offers(request):
    return render(request,'job_offers.html')





def companyRegister(request):
    if request.method == 'POST':
        
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phoneNo = form.cleaned_data['phoneNo']
            try:
                customuser = CustomUser.objects.create_user(username = username,email = email,password=password,phoneNo=phoneNo,user_type = 'company')
            except:
                form.add_error('email', 'Email is already in use or invalid.')
                return render(request, 'company_register_form.html', {'form': form})

            
            industry = form.cleaned_data['industry']
            location = form.cleaned_data['location']
            website = form.cleaned_data['website']
        
            try:
                user_data = CompanyUser.objects.create(account = customuser,industry=industry,location=location,website=website)
            except:
                form.add_error(None, 'Failed to create company details. Please try again.')
                customuser.delete()
                return render(request, 'company_register_form.html', {'form': form})

            
            
           
            return redirect('login')
    else:
        
        form = CompanyRegisterForm()

    context = {'form':form}
    
    return render(request,'company_register_form.html',context)

def Logout (request):
    logout(request)
    return redirect("login")


@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = email,password = password)

        if user is not None:
            login(request,user)
            if user.user_type == 'job_seeker':
                return redirect('profile')
            elif user.user_type == 'company':
                return redirect('company_profile')
            
        
        else:
            messages.error(request, "this account doesn't exist")
            return redirect('login')
    return render(request,'user_login.html')

def userRegister(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phoneNo = form.cleaned_data['phoneNo']
            try:
                customuser = CustomUser.objects.create_user(username = username,email = email,password=password,phoneNo=phoneNo,user_type = 'job_seeker')
            except:
                form.add_error('email', 'Email is already in use or invalid.')
                return render(request,'user_register_form.html', {'form': form})
            

            
            
            gender = form.cleaned_data['gender']
            
            try:
                user_data = NormalUser.objects.create(account = customuser,gender = gender)
            except:
                form.add_error(None,'Failed to create user details. Please try again.')
                customuser.delete()
                return render(request,'user_register_form.html', {'form': form})


            
            return redirect('login')
            
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request,'user_register_form.html',context)