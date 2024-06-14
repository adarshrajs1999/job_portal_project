from django.shortcuts import render, redirect
from job_portal_app.models import Employer
from job_portal_app.forms import employer_update_form


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
    employer_object.user.delete()
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



