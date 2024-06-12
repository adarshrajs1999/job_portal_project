from django.urls import path

from job_portal_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dash/', views.dash, name='dash'),
    path('admin_dash/', views.admin_dash, name='admin_dash'),
    path('employer_dash/', views.employer_dash, name='employer_dash'),
    path('jobseeker_dash/', views.jobseeker_dash, name='jobseeker_dash'),
    path('employer_register/', views.employer_register, name='employer_register'),


]