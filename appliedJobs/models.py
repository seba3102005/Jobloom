from django.db import models
from N_userProfile.models import NormalUser
from job.models import JobOffer
# Create your models here.


# adding new features

class MyAppliedJobs(models.Model):

    choices1 = (("3_months","3_months"),("6_months","6_months"),("every_year","every_year"))
    choices2 = (("5%","5%"),("10%","10%"),("15%","15%"))


    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE,related_name= 'user_jobs')
    job = models.ForeignKey(JobOffer,on_delete=models.CASCADE, related_name='candidates')
    cover_letter = models.TextField()
    salaryWithout = models.FloatField()
    salaryWithFees = models.FloatField()
    rate_increase = models.CharField(max_length=100,choices=choices1)
    increase_percentage = models.CharField(max_length=10,choices=choices2)
    date = models.DateField(auto_now_add=True)

    
    class Meta:
        unique_together = ('user','job')

    

