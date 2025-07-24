from django.shortcuts import render,redirect
from job.models import JobOffer,Skill
from .forms import JobForm,SkillForm
from user.models import CustomUser,CompanyUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from savedJobs.models import SavedJobs
from user.models import NormalUser
from appliedJobs.models import MyAppliedJobs
from appliedJobs.forms import applyForm

# Create your views here.

@login_required(login_url='login')
def GetJobOffers(request):
    data = JobOffer.objects.all()

    
    if request.user.user_type == 'job_seeker':
        normal_user = NormalUser.objects.get(account = request.user)
        saved_jobs_qs = SavedJobs.objects.filter(user=normal_user)
        user_saved_jobs = [entry.job.id for entry in saved_jobs_qs]
        
        context = {'data':data,'user': request.user,'user_saved_jobs':user_saved_jobs}
    else:
        context = {'data':data,'user': request.user,'company_user':CompanyUser.objects.get(account=request.user)}
   
        

    return render(request,'job_offers.html',context)


@login_required(login_url='login')
def status_filter (request):
    all_jobs = JobOffer.objects.all()
    if request.method=='GET':
        if 'search1' in request.GET:
            searchans = request.GET['search1']
            if searchans:
                all_jobs=all_jobs.filter(title__icontains=searchans)

        context = {'user':request.user,'data' : all_jobs}

    return render(request,'job_offers.html',context)

@login_required(login_url='login')
def job_details(request,id):
    data = JobOffer.objects.all().get(id = id)
    
        # try:
        #     saved_jobs = SavedJobs.objects.get(user = normal_user,job=id)
        # except:
        #     pass

    applied_users = MyAppliedJobs.objects.filter(job = id).count()
    if request.user.user_type == 'job_seeker':
        normal_user = NormalUser.objects.get(account = request.user)
        saved_jobs_qs = SavedJobs.objects.filter(user=normal_user)
        user_saved_jobs = [entry.job.id for entry in saved_jobs_qs]
        
        context = {'data':data,'user': request.user,'user_saved_jobs':user_saved_jobs,'applied_users':applied_users}
    else:
        context = {'data':data,'user': request.user,'applied_users':applied_users}

        
    return render(request,'job_details.html',context)

@login_required(login_url='login')  
def addJob(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
           
            job_offer = form.save(commit=False)
            company_user = CompanyUser.objects.get(account = request.user)
            job_offer.company = company_user
            job_offer.save()

            
            new_skills_text = form.cleaned_data.get('new_skills', '')
            skill_names = [name.strip() for name in new_skills_text.split(',') if name.strip()]

            
            job_offer.job_skill.clear()

            
            for skill_name in skill_names:
                skill_obj, created = Skill.objects.get_or_create(name=skill_name)
                job_offer.job_skill.add(skill_obj)

            data = JobOffer.objects.all()

            if request.user.user_type == 'job_seeker':
                context = {'data':data,'user': request.user}
            else:
                context = {'data':data,'user': request.user,'company_user':CompanyUser.objects.get(account=request.user)}
   
            return render(request,'job_offers.html',context)
    else:
        form = JobForm()

    return render(request, 'add_job.html', {'form': form})

@login_required(login_url='login')
def apply(request):
    data = JobOffer.objects.all()
    form = applyForm()
    context = {'data':data,'user': request.user,'form':form}
    return render(request,'apply.html',context)


@login_required(login_url='login')
@csrf_exempt  
def deleteJob(request, job_offer_id):
    
    if request.method == 'DELETE':
        
        try:
            experience = JobOffer.objects.get(id=job_offer_id)
            
            experience.delete()
            return JsonResponse({'success': True})
        except JobOffer.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


def deleteJobProfile(request,jobID):
        company_user = CompanyUser.objects.get(account = request.user)
        job = JobOffer.objects.get(company = company_user,id = jobID)
        job.delete()
        return redirect('company_profile')
