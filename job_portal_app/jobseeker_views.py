from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from job_portal_app.filters import Job_filterset
from job_portal_app.forms import feedback_form, jobseeker_profile_update_form
from job_portal_app.models import Jobseeker, Feedback, Job_post, Job_application, Shortlist, Interview, Hire



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
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request, 'jobseeker/jobseeker_feedback.html',{'feedback_form_data':feedback_form_data,'current_jobseeker_object':current_jobseeker_object})


def jobseeker_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request,'jobseeker/jobseeker_view_feedbacks.html',{'feedback_objects':feedback_objects,'current_jobseeker_object':current_jobseeker_object})


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
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request,"jobseeker/jobseeker_profile_update.html",{'jobseeker_profile_update_form_data':jobseeker_profile_update_form_data,'current_jobseeker_object':current_jobseeker_object})


def jobseeker_view_job_posts(request):
    job_post_objects = Job_post.objects.all()
    job_filterset_object = Job_filterset(request.GET, queryset = job_post_objects)
    job_post_objects = job_filterset_object.qs
    paginator = Paginator( job_post_objects, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request,"jobseeker/jobseeker_view_job_posts.html",{'page_obj':page_obj,'job_filterset_object':job_filterset_object,'current_jobseeker_object':current_jobseeker_object})


def job_apply(request, id):
    jobseeker_object = Jobseeker.objects.get(user = request.user)
    job_post_object = Job_post.objects.get(id = id)
    job_application_object = Job_application(jobseeker = jobseeker_object,job_post = job_post_object)
    job_application_object.save()
    job_post_object.apply_status = 1
    job_post_object.save()
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return redirect('jobseeker_view_job_posts')


def jobseeker_view_my_job_applications(request):
    job_application_objects = Job_application.objects.filter(jobseeker__user = request.user)
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request,'jobseeker/view_my_job_applications.html',{'job_application_objects':job_application_objects,'current_jobseeker_object':current_jobseeker_object})


def jobseeker_cancel_application_my(request, id):
    job_application_object = Job_application.objects.get(id = id)
    job_application_object.job_post.apply_status = 0
    job_application_object.job_post.save()
    job_application_object.delete()
    return redirect('jobseeker_view_my_job_applications')

def jobseeker_cancel_application_all(request,id):
    job_application_object = Job_application.objects.get(job_post__id = id)
    job_application_object.job_post.apply_status = 0
    job_application_object.job_post.save()
    job_application_object.delete()
    return redirect('jobseeker_view_job_posts')

def jobseeker_view_my_shortlisted_applications(request):
    shortlist_objects = Shortlist.objects.filter(job_application__jobseeker__user = request.user)
    current_jobseeker_object = Jobseeker.objects.get(user = request.user)
    return render(request, 'jobseeker/jobseeker_view_my_shortlisted_applications.html',{'shortlist_objects':shortlist_objects, 'current_jobseeker_object':current_jobseeker_object})


def jobseeker_view_interviews_sheduled_for_me(request):
    interview_objects = Interview.objects.filter(shortlist__job_application__jobseeker__user = request.user)
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request, 'jobseeker/jobseeker_view_interviews_sheduled_for_me.html',{'interview_objects':interview_objects,'current_jobseeker_object':current_jobseeker_object})

def jobseeker_view_interview_shedule(request, id):
    interview_object = Interview.objects.get(id = id)
    if request.method == 'POST':
        interview_task_answer_link = request.POST.get('interview_task_answer_link')
        interview_object.interview_task_answer_link = interview_task_answer_link
        interview_object.save()
        return redirect('jobseeker_view_interview_shedule', id = interview_object.id)
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request, 'jobseeker/jobseeker_view_interview_shedule.html',{'interview_object':interview_object,'current_jobseeker_object':current_jobseeker_object})

def jobseeker_view_my_hired_applications(request):
    hire_objects = Hire.objects.filter(interview__shortlist__job_application__jobseeker__user = request.user)
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request,'jobseeker/jobseeker_check_email_for_my_hired_applications.html',{'hire_objects':hire_objects,'current_jobseeker_object':current_jobseeker_object})

