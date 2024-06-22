from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from job_portal_app.forms import employer_profile_update_form, job_post_form, job_post_update_form, interview_form
from job_portal_app.models import Employer, Job_post, Job_application, Jobseeker, Shortlist


@login_required(login_url = 'login_view')
def employer_profile_update(request):
    employer_object = Employer.objects.get(user=request.user)
    employer_profile_update_form_data = employer_profile_update_form(instance=employer_object)
    if request.method == 'POST':
        employer_profile_update_form_data = employer_profile_update_form(request.POST, instance=employer_object)
        if employer_profile_update_form_data.is_valid():
            employer_profile_update_form_data.save()
            return redirect('employer_profile_update')
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, "employer/employer_profile_update.html",
                  {'employer_profile_update_form_data': employer_profile_update_form_data,
                   'current_employer_object': current_employer_object})


@login_required(login_url = 'login_view')
def employer_add_job_post(request):
    employer_object = Employer.objects.get(user=request.user)
    job_post_form_object = job_post_form()
    if request.method == 'POST':
        job_post_form_object = job_post_form(request.POST, request.FILES)
        if job_post_form_object.is_valid():
            job_post_object = job_post_form_object.save(commit=False)
            job_post_object.employer = employer_object
            job_post_object.save()
            return redirect('employer_dash')
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, 'employer/employer_add_job_post.html',
                  {'job_post_form_object': job_post_form_object, 'current_employer_object': current_employer_object})


@login_required(login_url = 'login_view')
def employer_view_my_job_posts(request):
    job_post_objects = Job_post.objects.filter(employer__user=request.user)
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, "employer/employer_view_my_job_posts.html",
                  {'job_post_objects': job_post_objects, 'current_employer_object': current_employer_object})


@login_required(login_url = 'login_view')
def employer_job_post_update(request, id):
    job_post_object = Job_post.objects.get(id=id)
    job_post_update_form_object = job_post_update_form(instance=job_post_object)
    if request.method == 'POST':
        job_post_update_form_object = job_post_update_form(request.POST, request.FILES, instance=job_post_object)
        if job_post_update_form_object.is_valid():
            job_post_update_form_object.save()
            return redirect('employer_view_my_job_posts')
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, "employer/employer_job_post_update.html",
                  {'job_post_update_form_object': job_post_update_form_object,
                   'current_employer_object': current_employer_object})


@login_required(login_url = 'login_view')
def employer_job_post_delete(request, id):
    job_post_object = Job_post.objects.get(id=id)
    job_post_object.delete()
    return redirect('employer_view_my_job_posts')


@login_required(login_url = 'login_view')
def employer_view_job_applications(request):
    job_application_objects = Job_application.objects.filter(job_post__employer__user=request.user)
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, "employer/employer_view_job_applications.html",
                  {'job_application_objects': job_application_objects,
                   'current_employer_object': current_employer_object})


@login_required(login_url = 'login_view')
def employer_view_applicants_details(request, id):
    job_application_object = Job_application.objects.get(id=id)
    jobseeker_object = job_application_object.jobseeker
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, "employer/employer_view_applicants_details.html",
                  {'jobseeker_object': jobseeker_object, 'job_application_object':job_application_object , 'current_employer_object': current_employer_object})


def employer_shortlist_application(request, id):
    employer_object = Employer.objects.get(user = request.user)
    job_application_object = Job_application.objects.get(id = id)
    shortlist_object = Shortlist(employer = employer_object, job_application = job_application_object)
    shortlist_object.save()
    job_application_object.is_shortlisted = 1
    job_application_object.save()
    return redirect('employer_view_job_applications')

def employer_view_my_shortlisted_job_applications(request):
    shortlist_objects = Shortlist.objects.filter(employer__user = request.user)
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request,'employer/employer_view_my_shortlisted_job_applications.html',{'shortlist_objects':shortlist_objects,'current_employer_object':current_employer_object})


def employer_create_interview_shedule(request, id):
    shortlist_object = Shortlist.objects.get(id= id)
    interview_form_object = interview_form()
    if request.method == 'POST':
        interview_form_object = interview_form(request.POST)
        if interview_form_object.is_valid():
            interview_object = interview_form_object.save(commit = False)
            interview_object.shortlist = shortlist_object
            interview_object.save()
            shortlist_object.is_interview_created = 1
            shortlist_object.save()
            return redirect('employer_view_my_shortlisted_job_applications')
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, 'employer/employer_create_interview_shedule.html',{'interview_form_object':interview_form_object,'current_employer_object':current_employer_object})