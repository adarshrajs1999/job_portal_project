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
    profile_picture = models.FileField(upload_to = 'my_files',blank = True,null = True)

    def __str__(self):
        return self.name

class Jobseeker(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE, related_name = 'job_seeker_user')
    name = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 12)
    email = models.EmailField()
    profile_picture = models.FileField(upload_to = 'my_files',blank = True,null = True)
    resume= models.FileField(upload_to = 'my_files',blank = True,null = True)
    qualification = models.CharField(max_length = 250)
    bio = models.TextField()
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Job_post(models.Model):
    employer = models.ForeignKey(Employer,on_delete = models.CASCADE,related_name = "job_post_jobseeker")
    poster_image = models.FileField(upload_to = 'my_files')
    job_roles = models.CharField(max_length = 500)
    job_description = models.TextField()
    requirements = models.TextField()
    educational_qualification = models.CharField(max_length=250)
    application_last_date = models.DateField()
    posted_date = models.DateField(auto_now=True)
    apply_status = models.IntegerField(default = 0)


class Job_application(models.Model):
    jobseeker = models.ForeignKey(Jobseeker,on_delete=models.CASCADE,related_name = "job_application_jobseeker")
    job_post = models.ForeignKey(Job_post,on_delete=models.CASCADE,related_name = 'job_application_job_post')
    is_shortlisted = models.BooleanField(default = 0)


class Shortlist(models.Model):
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    job_application = models.ForeignKey(Job_application, on_delete = models.CASCADE)
    is_interview_created = models.BooleanField(default = 0)


class Interview(models.Model):
    shortlist = models.ForeignKey(Shortlist,on_delete = models.CASCADE)
    interview_date = models.DateField()
    detail = models.TextField()
    online_meet_link = models.CharField(max_length=250)
    interview_task_answer_link = models.CharField(blank = True,null = True)
    is_hired = models.BooleanField(default = 0)
    is_rejected = models.BooleanField(default = 0)
    is_mailed = models.BooleanField(default = 0)


class Hire(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    message = models.TextField()
    attachment = models.FileField(blank=True,null=True)
    address_and_contact = models.TextField()

class Feedback(models.Model):
    jobseeker = models.ForeignKey(Jobseeker,on_delete = models.CASCADE,related_name = 'feedback_jobseeker')
    date = models.DateField(auto_now = True)
    subject = models.CharField(max_length = 250)
    feedback = models.TextField()
    # None-->for python,null-->for database column to indicate the absence of value
    reply = models.TextField(blank = True, null = True)








































