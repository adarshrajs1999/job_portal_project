from django.shortcuts import redirect, render

from job_portal_app.filters import Job_filterset
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
    job_filterset_object = Job_filterset(request.GET, queryset = job_post_objects)
    job_post_objects = job_filterset_object.qs
    return render(request,"jobseeker/jobseeker_view_job_posts.html",{'job_post_objects':job_post_objects,'job_filterset_object':job_filterset_object})

def job_apply(request, id):
    jobseeker_object = Jobseeker.objects.get(user = request.user)
    job_post_object = Job_post.objects.get(id = id)
    job_application_object = Job_application(jobseeker = jobseeker_object,job_post = job_post_object)
    job_application_object.save()
    job_post_object.apply_status = 1
    job_post_object.save()
    return redirect('jobseeker_view_job_posts')

def jobseeker_view_my_job_applications(request):
    jobseeker_object = Jobseeker.objects.get(user = request.user)
    job_application_objects = Job_application.objects.filter(jobseeker = jobseeker_object)
    return render(request,'jobseeker/view_my_job_applications.html',{'job_application_objects':job_application_objects})





