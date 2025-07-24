from django.db import models
from user.models import NormalUser
from job.models import JobOffer
# Create your models here.

class Education(models.Model):
    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE,related_name='my_education')
    institution = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=10)
    def __str__(self):
        return self.institution


class Languages(models.Model):
    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE,related_name = 'my_languages')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class project(models.Model):
    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE,related_name='my_projects')
    name = models.CharField(max_length=200)
    image = models.URLField()
    def __str__(self):
        return self.name


class Certification(models.Model):
    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE,related_name='my_certifications')
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE,related_name='my_experience')
    description = models.TextField(max_length=100)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skills(models.Model):
    user = models.ForeignKey(NormalUser,on_delete=models.CASCADE,related_name='my_skills')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


