from django.db import models
from user.models import NormalUser
from job.models import JobOffer
# Create your models here.


class SavedJobs(models.Model):
    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE)
    job = models.ForeignKey(JobOffer,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','job')
    