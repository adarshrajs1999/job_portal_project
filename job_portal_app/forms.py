from django import forms

from job_portal_app.models import Employer


class employer_register_form(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('__all__')
        exclude = ('user', ' admin_approval_status')
