from django.db import models
from user.models import CompanyUser
# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class JobOffer(models.Model):
    exp_choices = [('entry_level','entry_level'),('intermediate','intermediate'),('expert','expert')]
    company = models.ForeignKey(CompanyUser,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    hourly_rate = models.CharField(max_length=100)
    experience = models.CharField(choices=exp_choices,max_length=20)
    job_skill = models.ManyToManyField(Skill)
    posted_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

