from django.shortcuts import render,redirect
from .forms import EmployeeForm,JobForm
from user.models import CustomUser,CompanyUser
from django.http import HttpResponse
from .models import Employee,Job
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from job.models import JobOffer


# Create your views here.


@login_required(login_url='login')
def profile(request):
    custom_user = CustomUser.objects.get(id=request.user.id)
    company_user = custom_user.company_account  
    
    return render(request,'company_profile.html',{
                  'industry':company_user.industry,
                  'location':company_user.location,
                  'website' : company_user.website,
                  'title' : company_user.title,
                  'description' : company_user.description,
                  'support_hours' : company_user.support_hours,
                  'username' : custom_user.username,
                  'employees' : Employee.objects.all().filter(company=company_user),
                  'jobs' : Job.objects.all().filter(company=company_user),
                  'job_offer_data': JobOffer.objects.filter(company = company_user),
                  'job_counts':JobOffer.objects.filter(company = company_user).count(),
                  
    }
    )



@login_required(login_url='login')
@csrf_exempt  
def deleteEmployee(request, emp_id):
    if request.method == 'DELETE':
        try:
            employee = Employee.objects.get(id=emp_id)
            employee.delete()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@login_required(login_url='login')
@csrf_exempt  
def deleteJob(request, job_id):
    if request.method == 'DELETE':
        try:
            job = Job.objects.get(id=job_id)
            
            job.delete()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@login_required(login_url='login')
def updateTitle(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)  

        company_user = custom_user.company_account
        data = request.POST.get('title')  
        if data:
            company_user.title = data
            company_user.save()
            return redirect('company_profile')  

        return HttpResponse("No title data provided", status=400)

    return redirect('company_profile') 

@login_required(login_url='login')
def updateLocation(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)  

        company_user = custom_user.company_account
        data = request.POST.get('location')  
        if data:
            company_user.location = data
            company_user.save()
            return redirect('company_profile')  

        return HttpResponse("No location data provided", status=400)

    return redirect('company_profile') 


@login_required(login_url='login')
def updateSupportHours(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)  

        company_user = custom_user.company_account
        data = request.POST.get('support_hours')  
        if data:
            company_user.support_hours = data
            company_user.save()
            return redirect('company_profile')  

        return HttpResponse("No support_hours data provided", status=400)

    return redirect('company_profile') 






@login_required(login_url='login')
def updateDescription(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)  

        company_user = custom_user.company_account
        data = request.POST.get('description')  
        if data:
            company_user.description = data
            company_user.save()
            return redirect('company_profile')  

        return HttpResponse("No description data provided", status=400)

    return redirect('company_profile') 





@login_required(login_url='login')
def addEmployee(request):
    if request.method == 'POST':
        
        form = EmployeeForm(request.POST, request.FILES)
        

        if form.is_valid():
            
            employee = form.save(commit=False)
            

            custom_user = CustomUser.objects.get(id=request.user.id)
            company_user = custom_user.company_account
            normal_user = CompanyUser.objects.get(id=company_user.id)

            employee.company = normal_user
            employee.save()
            

            image_url = employee.image if employee.image else ''

            return JsonResponse({
                'ok': True,
                'id': employee.id,
                'name': employee.name,
                'position': employee.position,
                'image': image_url,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)


def addjob(request):
    if request.method == 'POST':
        

        
        form = JobForm(request.POST, request.FILES)
        
        if form.is_valid():
            job = form.save(commit=False)
            

            custom_user = CustomUser.objects.get(id=request.user.id)
            company_user = custom_user.company_account
            normal_user = CompanyUser.objects.get(id=company_user.id)

            job.company = normal_user
            job.save()
            

            image_url = job.image if job.image else ''

            return JsonResponse({
                'ok': True,
                'id': job.id,
                'name': job.name,
                'description': job.description,
                'image': image_url,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)

            

