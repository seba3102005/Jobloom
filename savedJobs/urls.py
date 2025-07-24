from django.urls import path,include
from . import views

urlpatterns = [
    path('save/<int:jobID>/',views.saveJob,name="save_job"),
    path('unsave/<int:jobID>/',views.unsaveJob,name="unsave_job"),
    path('unsave/details/<int:jobID>/',views.unsaveJobInDetails,name="unsave_job_details"),
    path('save/details/<int:jobID>/',views.saveJobInDetails,name='save_job_details'),
    path('unsave/profile/<int:jobID>/',views.unsaveJobProfile,name='unsave_job_profile'),
]