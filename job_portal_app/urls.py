from django.urls import path

from job_portal_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dash/', views.dash, name='dash'),
    path('admin_dash/', views.admin_dash, name='admin_dash'),
    path('employer_dash/', views.employer_dash, name='employer_dash'),
    path('login_page/', views.login_page, name='login_page'),
    path('jobseeker_dash/', views.jobseeker_dash, name='jobseeker_dash'),
    path('employer_register/', views.employer_register, name='employer_register'),
    path('jobseeker_register/', views.jobseeker_register, name='jobseeker_register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view')

]