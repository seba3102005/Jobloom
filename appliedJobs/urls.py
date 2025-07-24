from django.urls import path,include
from . import views

urlpatterns = [
    path('job/<int:jobID>/',views.applyOnJob,name="apply_on_job"),
    path('myJobs/',views.myAppliedJobsfunc,name='my jobs'),
    
]