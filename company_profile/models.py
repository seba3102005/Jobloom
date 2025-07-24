from django.db import models
from user.models import CompanyUser
# Create your models here.

class Employee(models.Model):
    company = models.ForeignKey(CompanyUser,on_delete=models.CASCADE,related_name='company_employees')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.URLField(max_length=1000)

class Job(models.Model):
    company = models.ForeignKey(CompanyUser,on_delete=models.CASCADE,related_name='company_jobs')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()

