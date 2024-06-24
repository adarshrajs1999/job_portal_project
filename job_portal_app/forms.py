from django import forms

from job_portal_app.models import Employer, User_model, Jobseeker, Feedback, Job_post, Interview, Hire
from django.contrib.auth.forms import UserCreationForm

class date_input(forms.DateInput):
    input_type = 'date'

class user_form(UserCreationForm):
    username = forms.CharField(label = "username",widget = forms.TextInput(attrs = {'placeholder':'username'}))
    password1 = forms.CharField(label = "password",widget = forms.PasswordInput(attrs = {'placeholder':'password'}))
    password2 = forms.CharField(label = "Confirm password",widget = forms.PasswordInput(attrs = {'placeholder':'confirm password'}))
    class Meta:
        model = User_model
        fields = ('username','password1','password2')


class employer_form(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('__all__')
        exclude = ('user', 'admin_approval_status')

class jobseeker_form(forms.ModelForm):
    dob = forms.DateField(widget = date_input())
    class Meta:
        model = Jobseeker
        fields = ('__all__')
        exclude = ('user',)

class employer_update_form(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('__all__')
        exclude = ('user', 'admin_approval_status')

class jobseeker_update_form(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ('__all__')
        exclude = ('user',)

class feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('__all__')
        exclude = ('jobseeker','reply')

class employer_profile_update_form(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('__all__')
        exclude = ('user','admin_approval_status')

class jobseeker_profile_update_form(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ('__all__')
        exclude = ('user',)


class job_post_form(forms.ModelForm):
    application_last_date = forms.DateField(widget = date_input())
    class Meta:
        model = Job_post
        fields = ('__all__')
        exclude = ('employer','apply_status')

class job_post_update_form(forms.ModelForm):
    class Meta:
        model = Job_post
        fields = ('__all__')
        exclude = ('employer',)

class interview_form(forms.ModelForm):
    interview_date = forms.DateField(widget = date_input)
    interview_task_answer_link = forms.CharField(required = False, widget = forms.TextInput(attrs = {'readonly':'readonly'}))
    class Meta:
        model = Interview
        fields = ('__all__')
        exclude = ('shortlist','is_hired','is_rejected','is_mailed')

class hire_form(forms.ModelForm):
    class Meta:
        model = Hire
        fields = ('__all__')
        exclude = ('interview',)