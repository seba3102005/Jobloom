from django.urls import path,include
from . import views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('add/education/',views.addEducation,name='add_education'),
    path('add/language/',views.addLanguage,name='add_language'),
    path('add/skill/',views.addSkill,name='add_skill'),
    path('add/experience/',views.addExperience,name='add_experience'),
    path('add/certification/',views.addCertification,name='add_certification'),
    path('add/project/',views.addProject,name='add_project'),
    path('update/title/',views.update_title,name = 'update_title'),
    path('update/description/',views.update_description,name = 'update_description'),
    path('update/rate/',views.update_rate,name = 'update_rate'),
    path('update/video/',views.update_video,name = 'update_video'),
    path('update/hours/',views.update_hours_week,name = 'update_hours_week'),
    path('delete/skill/<int:skill_id>/',views.deleteSkill,name = 'delete_skill'),
    path('delete/language/<int:lang_id>/',views.deleteLanguage,name = 'delete_language'),
    path('delete/education/<int:education_id>/',views.deleteEducation,name='delete_education'),
    path('delete/certification/<int:cer_id>/',views.deleteCertification,name='delete_certification'),
    path('delete/experience/<int:ex_id>/',views.deleteExperience,name='delete_experience'),
    path('delete/project/<int:proj_id>/',views.deleteProject,name='delete_project'),
    
   
]