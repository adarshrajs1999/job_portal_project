import django_filters
from django import forms
from django_filters import FilterSet,CharFilter

from job_portal_app.models import Job_post


class Job_filterset(FilterSet):
    educational_qualification = CharFilter(lookup_expr = 'icontains',widget = forms.TextInput(attrs = {'placeholder':"Search by qualification",'class':'form-control'}))
    class Meta:
        model = Job_post
        fields = ['educational_qualification',]