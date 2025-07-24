from django.urls import path,include
from . import views
urlpatterns = [
    path('profile/',views.profile,name='company_profile'),
    path('add/employee/',views.addEmployee,name='add_employee'),
    path('add/job/',views.addjob,name='add_job'),
    path('update/title/',views.updateTitle,name='add_title'),
    path('update/description/',views.updateDescription,name='add_description'),
    path('update/location/',views.updateLocation,name='add_location'),
    path('update/hours/',views.updateSupportHours,name='add_support_hours'),
    path('delete/<int:emp_id>/',views.deleteEmployee,name='delete_employee'),
    path('delete/job/<int:job_id>/',views.deleteJob,name='delete_job'),
    

]