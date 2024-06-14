from django.shortcuts import redirect, render

from job_portal_app.forms import feedback_form
from job_portal_app.models import Jobseeker


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