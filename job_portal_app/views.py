from django.shortcuts import render, redirect

from job_portal_app.forms import employer_register_form


# Create your views here.

def home(request):
    return render(request, 'home.html')

def dash(request):
    return render(request,'dash.html')

def admin_dash(request):
    return render(request,'admin/admin_dash.html')

def employer_dash(request):
    return render(request,'employer/employer_dash.html')

def jobseeker_dash(request):
    return render(request,'jobseekr/jobseeker.html')

def login_page(request):
    return render(request,'login.html')

def employer_register(request):
    employer_register_form_data = employer_register_form()
    if request.method == 'POST':
        employer_register_form_data = employer_register_form(request.POST, request.FILES)
        if employer_register_form_data.is_valid():
            return redirect('/')
    return render(request,"employer_register.html",{'employer_register_form_data':employer_register_form_data})