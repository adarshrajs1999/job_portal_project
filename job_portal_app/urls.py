from django.urls import path

from job_portal_app import views, admin_views

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
    path('logout/', views.logout_view, name='logout_view'),
    path('employer_approval_requests/', admin_views.employer_approval_requests, name='employer_approval_requests'),
    path('approve_employer/<int:id>/', admin_views.approve_employer, name='approve_employer'),
    path('admin_employer_details/', admin_views.admin_employer_details, name='admin_employer_details'),
    path('employer_update/<int:pk>/', admin_views.admin_update_employer, name='admin_update_employer')

]