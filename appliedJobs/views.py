from django.shortcuts import render,redirect
from .models import MyAppliedJobs
from .forms import applyForm
from user.models import NormalUser
from job.models import JobOffer
from django.contrib import messages

# Create your views here.


def applyOnJob(request,jobID):
    if request.method == 'POST':
        form = applyForm(request.POST)
        if form.is_valid():
            apply_job = form.save(commit=False)
            normal_user = NormalUser.objects.get(account = request.user.id)
            apply_job.user = normal_user
            

            apply_job.job = JobOffer.objects.get(id = jobID)
            
            try:
                form.save()
                messages.success(request,'you have applied successfully to this job')
                return redirect('job_offers')
            except:
                messages.warning(request, 'You have applied to this job before.')
                return redirect('job_offers')
                
            
            
        else:
            print('form is not valid')
            messages.warning('you have applied to this job before')
            
        
    
    form = applyForm()
    return render(request,'apply.html',{'form':form,'jobID':jobID})


def myAppliedJobsfunc(request):
    if request.method == 'GET':
        normal_user = NormalUser.objects.get(account = request.user)
        my_jobs = MyAppliedJobs.objects.filter(user = normal_user).select_related('job')
        print(list(my_jobs.values('id','cover_letter','salaryWithout','salaryWithFees','job__title','job__description',)))
        data = JobOffer.objects.all()
        context = {'data':data,'user': request.user}
        return render(request,'job_offers.html',context)
    

