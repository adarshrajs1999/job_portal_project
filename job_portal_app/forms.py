from django import forms

from job_portal_app.models import Employer, User_model, Jobseeker, Feedback, Job_post
from django.contrib.auth.forms import UserCreationForm

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

class date_input(forms.DateInput):
    input_type = 'date'

class job_post_form(forms.ModelForm):
    application_last_date = forms.DateField(widget = date_input())
    class Meta:
        model = Job_post
        fields = ('__all__')
        exclude = ('employer',)

class job_post_update_form(forms.ModelForm):
    class Meta:
        model = Job_post
        fields = ('__all__')
        exclude = ('employer',)



