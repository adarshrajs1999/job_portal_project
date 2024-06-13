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
    profile_picture = models.FileField(upload_to = 'clients_docs')

    def __str__(self):
        return self.name

class Jobseeker(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE, related_name = 'job_seeker_user')
    name = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 12)
    email = models.EmailField()
    profile_picture = models.FileField()

    def __str__(self):
        return self.name

























