from django.shortcuts import render, redirect

from job_portal_app.forms import employer_profile_update_form, job_post_form
from job_portal_app.models import Employer, Job_post


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