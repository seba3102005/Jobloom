from django.urls import path,include
from . import  views

urlpatterns = [
    path('job_offers/',views.GetJobOffers,name='job_offers'),
    path('search_bar/',views.status_filter,name='search_bar'),
    path('details/<int:id>/',views.job_details,name = 'job_details'),
    path('add_job/',views.addJob,name='add_job2'),
    path('apply/',views.apply,name='apply'),
    path('delete/job/<int:job_offer_id>/',views.deleteJob,name='delete_job_offer'),
    path('delete/job/profile/<int:jobID>/',views.deleteJobProfile,name='delete_job_profile'),
    
]