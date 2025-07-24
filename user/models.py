from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class NewUserManager(BaseUserManager):

    def create_user(self,email,password,phoneNo,username,**kwargs):
        if not email:
            raise ValueError('You must provide an email address')
        norm_email = self.normalize_email(email)
     
        kwargs.setdefault('is_active', True)
        
        user = self.model(email=norm_email,phoneNo=phoneNo,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,username,phoneNo,**kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email=email,username=username,password=password,phoneNo=phoneNo ,**kwargs)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    type_choices = [('job_seeker','job_seeker'),('company','company')]
    
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phoneNo = models.CharField(max_length=11)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)   # by default is false when i want to implement that user can activate it account
    user_type = models.CharField(choices=type_choices,max_length=10)
    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('phoneNo','username')

    def __str__(self):
        return self.username

class NormalUser(models.Model):
    choices = [('male','male'),('female','female')]

    account = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='user_account')
    gender = models.CharField(max_length=10,choices=choices)
    first_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(('about'), max_length=500, blank=True)
    title = models.CharField(max_length=100,default='Title')
    description = models.TextField(max_length=500,default='Description')
    hourly_rate = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)],default=1)
    hours_week = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(30)],default=1)
    video = models.URLField(null=True)
    


class CompanyUser(models.Model):
    account = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='company_account')
    industry = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    website = models.URLField()
    title = models.CharField(max_length=100,default='Title')
    description = models.TextField(default='Description')
    support_hours = models.CharField(max_length=100,default='Mon - Fri, 9am to 6pm')


# class JobPost(models.Model):
#     company = models.ForeignKey(CompanyUser,on_delete=models.CASCADE,related_name='job_company')

#     title = models.CharField(max_length=50)
#     description = models.TextField()
#     opened = models.BooleanField(default=True)
#     image = models.ImageField(upload_to='photos/')

    

    





