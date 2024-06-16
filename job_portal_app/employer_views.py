from django.shortcuts import render, redirect

from job_portal_app.forms import employer_profile_update_form, job_post_form, job_post_update_form
from job_portal_app.models import Employer, Job_post, Job_application


def employer_profile_update(request):
    employer_object = Employer.objects.get(user = request.user)
    employer_profile_update_form_data = employer_profile_update_form(instance = employer_object)
    if request.method == 'POST':
        employer_profile_update_form_data = employer_profile_update_form(request.POST,instance = employer_object)
        if employer_profile_update_form_data.is_valid():
            employer_profile_update_form_data.save()
            return redirect('employer_profile_update')
    return render(request,"employer/employer_profile_update.html",{'employer_profile_update_form_data':employer_profile_update_form_data})

def employer_add_job_post(request):
    employer_object = Employer.objects.get(user = request.user)
    job_post_form_object = job_post_form()
    if request.method == 'POST':
        job_post_form_object = job_post_form(request.POST, request.FILES)
        if job_post_form_object.is_valid():
            job_post_object = job_post_form_object.save(commit = False)
            job_post_object.employer = employer_object
            job_post_object.save()
            return redirect('employer_dash')
    return render(request,'employer/employer_add_job_post.html',{'job_post_form_object':job_post_form_object})

def employer_view_my_job_posts(request):
    current_employer_object = Employer.objects.get(user = request.user)
    job_post_objects= Job_post.objects.filter(employer = current_employer_object)
    return render(request,"employer/employer_view_my_job_posts.html",{'job_post_objects':job_post_objects})

def employer_job_post_update(request, id):
    job_post_object = Job_post.objects.get(id =id)
    job_post_update_form_object = job_post_update_form(instance = job_post_object)
    if request.method == 'POST':
        job_post_update_form_object = job_post_update_form(request.POST,request.FILES,instance = job_post_object)
        if job_post_update_form_object.is_valid():
            job_post_update_form_object.save()
            return redirect('employer_view_my_job_posts')
    return render(request,"employer/employer_job_post_update.html",{'job_post_update_form_object':job_post_update_form_object})

def employer_job_post_delete(request, id):
    job_post_object =Job_post.objects.get(id =id)
    job_post_object.delete()
    return redirect('employer_view_my_job_posts')

def employer_view_job_applications(request):
    job_application_objects = Job_application.objects.all()
    return render(request,"employer/employer_view_job_applications.html",{'job_application_objects':job_application_objects})

def employer_view_applicants_details(request, id):
    job_application_object = Job_application.objects.get(id = id)
    jobseeker_object = job_application_object.jobseeker
    return render(request,"employer/employer_view_applicants_details.html",{'jobseeker_object':jobseeker_object})



