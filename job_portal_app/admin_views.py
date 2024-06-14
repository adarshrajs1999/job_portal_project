from django.shortcuts import render, redirect
from job_portal_app.models import Employer, Jobseeker, Feedback
from job_portal_app.forms import employer_update_form, jobseeker_update_form


def employer_approval_requests(request):
    employer_objects = Employer.objects.filter(admin_approval_status = 0)
    return render(request,"admin/admin_employer_approval_requests.html",{'employer_objects':employer_objects})

def approve_employer(request, id):
    employer_object = Employer.objects.get(id = id)
    employer_object.admin_approval_status = 1
    employer_object.save()
    return redirect('employer_approval_requests')

def remove_employer_request(request, id):
    employer_object = Employer.objects.get(id=id)
    user_object = employer_object.user
    user_object.delete()
    return redirect('employer_approval_requests')

def admin_employer_details(request):
    employer_objects = Employer.objects.filter(admin_approval_status = 1)
    return render(request, "admin/admin_employer_details.html",{'employer_objects':employer_objects})

def admin_employer_update(request, pk):
    employer_object = Employer.objects.get(pk=pk)
    employer_update_form_data = employer_update_form(instance = employer_object)
    if request.method == 'POST':
        employer_update_form_data = employer_update_form(request.POST, instance = employer_object)
        if employer_update_form_data.is_valid():
            employer_update_form_data.save()
            return redirect('admin_employer_details')
    return render(request, 'admin/employer_update.html',{'employer_update_form_data':employer_update_form_data})

def admin_employer_remove(request, id):
    employer_object = Employer.objects.get(id = id)
    employer_object.admin_approval_status = 0
    employer_object.save()
    return redirect('admin_employer_details')

def admin_jobseeker_details(request):
    jobseeker_objects = Jobseeker.objects.all()
    return render(request, "admin/admin_jobseeker_details.html",{'jobseeker_objects':jobseeker_objects})

def admin_jobseeker_update(request, pk):
    jobseeker_object = Jobseeker.objects.get(pk=pk)
    jobseeker_update_form_data = jobseeker_update_form(instance = jobseeker_object)
    if request.method == 'POST':
        jobseeker_update_form_data = jobseeker_update_form(request.POST, instance = jobseeker_object)
        if jobseeker_update_form_data.is_valid():
            jobseeker_update_form_data.save()
            return redirect('admin_jobseeker_details')
    return render(request, 'admin/admin_jobseeker_update.html',{'jobseeker_update_form_data':jobseeker_update_form_data})

def admin_jobseeker_delete(request, id):
    jobseeker_object = Jobseeker.objects.get(id = id)
    user_object = jobseeker_object.user
    user_object.delete()
    return redirect('admin_jobseeker_details')
def admin_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    return render(request,'admin/admin_view_feedbacks.html',{'feedback_objects':feedback_objects})

def admin_feedback_reply(request, id):
    feedback_object = Feedback.objects.get(id = id)
    if request.method == 'POST':
        reply = request.POST.get('reply')
        feedback_object.reply = reply
        feedback_object.save()
        return redirect('admin_view_feedbacks')
    return render(request,'admin/admin_feedback_reply.html',{'feedback_object':feedback_object})

def admin_feedback_delete(request, id):
    feedback_object = Feedback.objects.get(id=id)
    feedback_object.delete()
    return redirect('admin_view_feedbacks')