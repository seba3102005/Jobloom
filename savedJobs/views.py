from django.shortcuts import render,redirect
from user.models import NormalUser
from savedJobs.models import SavedJobs
from job.models import JobOffer
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


def saveJob(request,jobID):
    if request.method == 'GET':
        
        normal_user = NormalUser.objects.get(account=request.user)
        job = JobOffer.objects.get(id=jobID)


        try:
            SavedJobs.objects.create(user = normal_user,job=job)
            
            return JsonResponse({'saved':True})
        except:
            
            return JsonResponse({'saved':False})
            
        


def unsaveJob(request,jobID):
        
        normal_user = NormalUser.objects.get(account=request.user)
        
        job = SavedJobs.objects.get(user = normal_user,job = jobID)
        job.delete()
        return JsonResponse({'notsaved':True})
        



def unsaveJobInDetails(request,jobID):
        
        normal_user = NormalUser.objects.get(account=request.user)
        
        job = SavedJobs.objects.get(user = normal_user,job = jobID)
        job.delete()
        saved_jobs_qs = SavedJobs.objects.filter(user=normal_user)
        user_saved_jobs = [entry.job.id for entry in saved_jobs_qs]
        data = JobOffer.objects.get(id = jobID)
        context = {'data':data,'user': request.user,'user_saved_jobs':user_saved_jobs}
        return render(request,'job_details.html',context)



def saveJobInDetails(request,jobID):
    if request.method == 'GET':
        normal_user = NormalUser.objects.get(account=request.user)
        job = JobOffer.objects.get(id=jobID)

        SavedJobs.objects.create(user = normal_user,job=job)
        saved_jobs_qs = SavedJobs.objects.filter(user=normal_user)
        user_saved_jobs = [entry.job.id for entry in saved_jobs_qs]
        
        data = JobOffer.objects.get(id = jobID)
        context = {'data':data,'user': request.user,'user_saved_jobs':user_saved_jobs}
        return render(request,'job_details.html',context)


def unsaveJobProfile(request,jobID):
        
        normal_user = NormalUser.objects.get(account=request.user)
        job = SavedJobs.objects.get(user = normal_user,job = jobID)
        job.delete()
        

        context = {'user': request.user}
        return redirect('profile')

