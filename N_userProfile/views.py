from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import EducationForm,SkillForm,LanguageForm,WorkForm,CertificationForm,ProjectForm
from django.contrib.auth import get_user_model
from user.models import CustomUser,NormalUser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from N_userProfile.models import Education,Languages,Certification,WorkExperience,Skills,project
from django.http import JsonResponse
import json
from appliedJobs.models import MyAppliedJobs
from savedJobs.models import SavedJobs
# Create your views here.

user = get_user_model()


@login_required(login_url='login')
def profile(request):

    custom_user = CustomUser.objects.get(id=request.user.id)
    normal_user = custom_user.user_account  
    
    
    return render(request, 'profile.html', {
        'education_form': EducationForm(),
        'skill_form': SkillForm(),
        'language_form': LanguageForm(),
        'experience_form': WorkForm(),
        'certification_form': CertificationForm(),
        'project_form': ProjectForm(),
        'education_data':Education.objects.all().filter(user=normal_user),
        'languages_data':Languages.objects.all().filter(user=normal_user),
        'certification_data':Certification.objects.all().filter(user=normal_user),
        'work_data': WorkExperience.objects.all().filter(user=normal_user),
        'title':normal_user.title,
        'description':normal_user.description,
        'skill_data' : Skills.objects.all().filter(user=normal_user),
        'hours_week' : normal_user.hours_week,
        'video' : normal_user.video,
        'rate' : normal_user.hourly_rate,
        'project_data' : project.objects.all().filter(user=normal_user),
        'username': custom_user.username,
        'applied_jobs_data':MyAppliedJobs.objects.filter(user = normal_user).select_related('job'),
        'saved_jobs_data' : SavedJobs.objects.filter(user=normal_user)
    })


@login_required(login_url='login')
@csrf_exempt  
def deleteSkill(request, skill_id):
    if request.method == 'DELETE':
        
        try:
            skill = Skills.objects.get(id=skill_id)
            
            skill.delete()
            return JsonResponse({'success': True})
        except Skills.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

@login_required(login_url='login')
@csrf_exempt  
def deleteLanguage(request, lang_id):
    if request.method == 'DELETE':
        
        try:
            language = Languages.objects.get(id=lang_id)
            
            language.delete()
            return JsonResponse({'success': True})
        except Languages.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@login_required(login_url='login')
@csrf_exempt  
def deleteEducation(request, education_id):
    if request.method == 'DELETE':
        
        try:
            education = Education.objects.get(id=education_id)
            
            education.delete()
            return JsonResponse({'success': True})
        except Education.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@login_required(login_url='login')
@csrf_exempt  
def deleteCertification(request, cer_id):
    if request.method == 'DELETE':
        
        try:
            certification = Certification.objects.get(id=cer_id)
            
            certification.delete()
            return JsonResponse({'success': True})
        except Certification.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@login_required(login_url='login')
@csrf_exempt  
def deleteExperience(request, ex_id):
    
    if request.method == 'DELETE':
        
        try:
            experience = WorkExperience.objects.get(id=ex_id)
            
            experience.delete()
            return JsonResponse({'success': True})
        except WorkExperience.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@login_required(login_url='login')
@csrf_exempt  
def deleteProject(request, proj_id):
    
    if request.method == 'DELETE':
        
        try:
            projectt = project.objects.get(id=proj_id)
            
            projectt.delete()
            return JsonResponse({'success': True})
        except project.DoesNotExist:
            
            return JsonResponse({'success': False, 'error': 'Not found'}, status=404)
    
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

@login_required(login_url='login')
def update_description(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)
        normal_user = custom_user.user_account  
        data = request.POST.get('description')

        if data:
            normal_user.description = data
            normal_user.save()
            return redirect('profile')  

        return HttpResponse("No description data provided", status=400)

    return redirect('profile') 



@login_required(login_url='login')
def update_rate(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)
        normal_user = custom_user.user_account  
        data = request.POST.get('rate')

        if data:
            normal_user.hourly_rate = data
            normal_user.save()
            return redirect('profile')  

        return HttpResponse("No description data provided", status=400)

    return redirect('profile') 


@login_required(login_url='login')
def update_video(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)
        normal_user = custom_user.user_account  
        data = request.POST.get('video')

        if data:
            normal_user.video = data
            normal_user.save()
            return redirect('profile')  

        return HttpResponse("No description data provided", status=400)

    return redirect('profile') 


@login_required(login_url='login')
def update_hours_week(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)
        normal_user = custom_user.user_account  
        data = request.POST.get('hours_week')

        if data:
            normal_user.hours_week = data
            normal_user.save()
            return redirect('profile')  

        return HttpResponse("No description data provided", status=400)

    return redirect('profile') 



@login_required(login_url='login')
def update_title(request):
    if request.method == 'POST':
        custom_user = CustomUser.objects.get(id=request.user.id)
        normal_user = custom_user.user_account  
        data = request.POST.get('title')

        if data:
            normal_user.title = data
            normal_user.save()
            return redirect('profile')  

        return HttpResponse("No title data provided", status=400)

    return redirect('profile') 



@login_required(login_url='login')
def addEducation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = EducationForm(data)
        if form.is_valid():
            data = form.save(commit=False)
            custom_user = CustomUser.objects.get(id=request.user.id)
            normal_user = NormalUser.objects.get(id=custom_user.user_account.id)
            data.user = normal_user
            data.save()

            # Return JSON instead of redirect
            return JsonResponse({
                'ok':True,
                'id': data.id,
                'institution': data.institution,
                'graduation_year': str(data.graduation_year),
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    # If GET request, you can return nothing or the empty form if needed
    return JsonResponse({'error': 'Invalid request method'}, status=405)




@login_required(login_url='login')
def addSkill(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = SkillForm(data)
        if form.is_valid():
            data = form.save(commit=False)
            custom_user = CustomUser.objects.get(id=request.user.id)
            normal_user = NormalUser.objects.get(id=custom_user.user_account.id)
            data.user = normal_user
            data.save()

            
            return JsonResponse({
                'ok':True,
                'id': data.id,
                'name': data.name,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)





@login_required(login_url='login')
def addLanguage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = LanguageForm(data)
        if form.is_valid():
            data = form.save(commit=False)
            custom_user = CustomUser.objects.get(id=request.user.id)
            normal_user = NormalUser.objects.get(id=custom_user.user_account.id)
            data.user = normal_user
            data.save()

            return JsonResponse({
                'ok':True,
                'id': data.id,
                'name': data.name,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




@login_required(login_url='login')
def addExperience(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = WorkForm(data)
        if form.is_valid():
            data = form.save(commit=False)
            custom_user = CustomUser.objects.get(id=request.user.id)
            normal_user = NormalUser.objects.get(id=custom_user.user_account.id)
            data.user = normal_user
            data.save()

            return JsonResponse({
                'ok':True,
                'id':data.id,
                'description': data.description,
                'name': data.name,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@login_required(login_url='login')
def addCertification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = CertificationForm(data)
        if form.is_valid():
            data = form.save(commit=False)
            custom_user = CustomUser.objects.get(id=request.user.id)
            normal_user = NormalUser.objects.get(id=custom_user.user_account.id)
            data.user = normal_user
            data.save()

            return JsonResponse({
                'ok':True,
                'id':data.id,
                'organization': data.organization,
                'name': data.name,
                'year': data.year,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



@login_required(login_url='login')
def addProject(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = ProjectForm(data)
        if form.is_valid():
            data = form.save(commit=False)
            custom_user = CustomUser.objects.get(id=request.user.id)
            normal_user = NormalUser.objects.get(id=custom_user.user_account.id)
            data.user = normal_user
            data.save()

            
            return JsonResponse({
                'ok':True,
                'id': data.id,
                'name': data.name,
                'image': data.image,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)









