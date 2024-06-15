from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User_model(AbstractUser):
    is_employer = models.BooleanField(default = False)
    is_jobseeker = models.BooleanField(default = False)

class Employer(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE, related_name = 'employer_user')
    admin_approval_status = models.BooleanField(default = 0)
    name = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 12)
    email = models.EmailField()
    profile_picture = models.FileField(upload_to = 'my_files')

    def __str__(self):
        return self.name

class Jobseeker(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE, related_name = 'job_seeker_user')
    name = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 12)
    email = models.EmailField()
    profile_picture = models.FileField(upload_to = 'my_files')

    def __str__(self):
        return self.name

class Feedback(models.Model):
    jobseeker = models.ForeignKey(Jobseeker,on_delete = models.CASCADE,related_name = 'feedback_jobseeker')
    date = models.DateField(auto_now = True)
    subject = models.CharField(max_length = 250)
    feedback = models.TextField()
    # None-->for python,null-->for database column to indicate the absence of value
    reply = models.TextField(blank = True, null = True)

class Job_post(models.Model):
    employer = models.ForeignKey(Employer,on_delete = models.CASCADE,related_name = "job_post_jobseeker")
    image = models.FileField(upload_to = 'my_files')
    job_role = models.CharField(max_length = 250)
    qualification = models.CharField(max_length = 250)
    job_description = models.TextField()
    requirements = models.TextField()
    application_last_date = models.DateField()
    posted_date = models.DateField(auto_now=True)
























