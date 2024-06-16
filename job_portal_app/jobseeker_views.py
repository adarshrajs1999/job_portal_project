from django.shortcuts import redirect, render

from job_portal_app.forms import feedback_form, jobseeker_profile_update_form
from job_portal_app.models import Jobseeker, Feedback, Job_post, Job_application


def jobseeker_feedback(request):
    feedback_form_data = feedback_form()
    current_jobseeker_object = Jobseeker.objects.get(user = request.user)
    if request.method == 'POST':
        feedback_form_data = feedback_form(request.POST)
        if feedback_form_data.is_valid():
            feedback_object = feedback_form_data.save(commit = False)
            feedback_object.jobseeker = current_jobseeker_object
            feedback_object.save()
            return redirect('jobseeker_dash')
    return render(request, 'jobseeker/jobseeker_feedback.html',{'feedback_form_data':feedback_form_data})

def jobseeker_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    return render(request,'jobseeker/jobseeker_view_feedbacks.html',{'feedback_objects':feedback_objects})

def jobseeker_feedback_delete(request, id):
    feedback_object = Feedback.objects.get(id = id)
    feedback_object.delete()
    return redirect('jobseeker_view_feedbacks')

def jobseeker_profile_update(request):
    jobseeker_object = Jobseeker.objects.get(user = request.user)
    jobseeker_profile_update_form_data = jobseeker_profile_update_form(instance = jobseeker_object)
    if request.method == 'POST':
        jobseeker_profile_update_form_data = jobseeker_profile_update_form(request.POST,request.FILES,instance = jobseeker_object)
        if jobseeker_profile_update_form_data.is_valid():
            jobseeker_profile_update_form_data.save()
            return redirect('jobseeker_profile_update')
    return render(request,"jobseeker/jobseeker_profile_update.html",{'jobseeker_profile_update_form_data':jobseeker_profile_update_form_data})

def jobseeker_view_job_posts(request):
    job_post_objects = Job_post.objects.all()
    return render(request,"jobseeker/jobseeker_view_job_posts.html",{'job_post_objects':job_post_objects})

def job_apply(request, id):
    jobseeker_object = Jobseeker.objects.get(user = request.user)
    job_post_object = Job_post.objects.get(id =id)
    job_application_object = Job_application(jobseeker = jobseeker_object,job_post = job_post_object)
    job_application_object.save()
    job_application_object.job_post.apply_status = True
    return redirect('jobseeker_view_job_posts')







