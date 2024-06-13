from django.shortcuts import render

from job_portal_app.models import Employer


def admin_employer_details(request):
    employer_objects = Employer.objects.all()
    return render(request, "admin/admin_employer_details.html",{'employer_objects':employer_objects})