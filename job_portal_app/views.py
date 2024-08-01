from django.shortcuts import render, redirect
from job_portal_app.forms import employer_form, user_form, jobseeker_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from job_portal_app.models import Employer, Jobseeker


# Create your views here.


def home(request):
    return render(request, 'home.html')


def register_dash(request):
    return render(request, 'register_dash.html')

def user_dash(request):
    return render(request, 'user_dash.html')



def admin_dash(request):
    return render(request, 'admin/admin_dash.html')



def employer_dash(request):
    current_employer_object = Employer.objects.get(user=request.user)
    return render(request, 'employer/employer_dash.html', {'current_employer_object': current_employer_object})



def jobseeker_dash(request):
    current_jobseeker_object = Jobseeker.objects.get(user=request.user)
    return render(request, 'jobseeker/jobseeker_dash.html', {'current_jobseeker_object': current_jobseeker_object})



def login_page(request):
    return render(request, 'login.html')



def employer_register(request):
    user_form_data = user_form()
    employer_form_data = employer_form()
    if request.method == 'POST':
        user_form_data = user_form(request.POST)
        employer_form_data = employer_form(request.POST, request.FILES)
        if user_form_data.is_valid() and employer_form_data.is_valid():
            user_object = user_form_data.save(commit=False)
            user_object.is_employer = True
            user_object.save()
            employer_object = employer_form_data.save(commit=False)
            employer_object.user = user_object
            employer_object.save()
            return redirect('/')
    return render(request, "employer_register.html",
                  {'user_form_data': user_form_data, 'employer_form_data': employer_form_data})



def jobseeker_register(request):
    user_form_data = user_form()
    jobseeker_form_data = jobseeker_form()
    if request.method == 'POST':
        user_form_data = user_form(request.POST)
        jobseeker_form_data = jobseeker_form(request.POST, request.FILES)
        if user_form_data.is_valid() and jobseeker_form_data.is_valid():
            user_object = user_form_data.save(commit=False)
            user_object.is_jobseeker = True
            user_object.save()
            jobseeker_object = jobseeker_form_data.save(commit=False)
            jobseeker_object.user = user_object
            jobseeker_object.save()
            return redirect('/')
    return render(request, "job_seeker_register.html",
                  {'user_form_data': user_form_data, 'jobseeker_form_data': jobseeker_form_data})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_object = authenticate(username=username, password=password)
        if user_object is not None:
            if user_object.is_employer:
                employer_object = Employer.objects.get(user=user_object)
                if employer_object.admin_approval_status == 1:
                    login(request, user_object)
                    return redirect('employer_dash')
                else:
                    messages.info(request, "Currently this user is not approved by admin!")
            elif user_object.is_staff:
                login(request, user_object)
                return redirect('admin_dash')
            elif user_object.is_jobseeker:
                login(request, user_object)
                return redirect('jobseeker_dash')
        else:
            messages.info(request, "Invalid credentials!")
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login_view')
