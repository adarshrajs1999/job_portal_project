from django.shortcuts import render, redirect

from job_portal_app.forms import employer_form, user_form


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
    user_form_data = user_form()
    employer_form_data = employer_form()
    if request.method == 'POST':
        user_form_data = user_form(request.POST)
        employer_form_data = employer_form(request.POST, request.FILES)
        if user_form_data.is_valid() and employer_form_data.is_valid():
            user_object = user_form_data.save(commit = False)
            user_object.is_employer = True
            user_object.save()
            employer_object = employer_form_data.save(commit = False)
            employer_object.user = user_object
            employer_object.save()
            return redirect("/")
    return render(request,"employer_register.html",{'user_form_data':user_form_data,'employer_form_data':employer_form_data})