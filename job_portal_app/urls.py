from django.urls import path

from job_portal_app import views, admin_views, jobseeker_views, employer_views

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
    path('remove_employer_request/<int:id>/', admin_views.remove_employer_request, name='remove_employer_request'),
    path('approve_employer/<int:id>/', admin_views.approve_employer, name='approve_employer'),
    path('admin_employer_details/', admin_views.admin_employer_details, name='admin_employer_details'),
    path('admin_employer_update/<int:pk>/', admin_views.admin_employer_update, name='admin_employer_update'),
    path('admin_employer_remove/<int:id>/', admin_views.admin_employer_remove, name='admin_employer_remove'),
    path('admin_jobseeker_details/', admin_views.admin_jobseeker_details, name='admin_jobseeker_details'),
    path('admin_jobseeker_update/<int:pk>/', admin_views.admin_jobseeker_update, name='admin_jobseeker_update'),
    path('admin_jobseeker_delete/<int:id>/', admin_views.admin_jobseeker_delete, name='admin_jobseeker_delete'),
    path('jobseeker_feedback/', jobseeker_views.jobseeker_feedback, name='jobseeker_feedback'),
    path('admin_view_feedbacks/', admin_views.admin_view_feedbacks, name='admin_view_feedbacks'),
    path('admin_feedback_reply/<int:id>/', admin_views.admin_feedback_reply, name='admin_feedback_reply'),
    path('jobseeker_view_feedbacks/',jobseeker_views.jobseeker_view_feedbacks,name = 'jobseeker_view_feedbacks'),
    path('jobseeker_feedback_delete/<int:id>/', jobseeker_views.jobseeker_feedback_delete, name='jobseeker_feedback_delete'),
    path('admin_feedback_delete/<int:id>/',admin_views.admin_feedback_delete,name="admin_feedback_delete"),
    path('employer_profile_update/',employer_views.employer_profile_update,name = 'employer_profile_update'),
    path('jobseeker_profile_update/',jobseeker_views.jobseeker_profile_update,name = 'jobseeker_profile_update'),
    path('employer_add_job_post/',employer_views.employer_add_job_post,name="employer_add_job_post"),
    path('employer_view_my_job_posts',employer_views.employer_view_my_job_posts,name="employer_view_my_job_posts"),
    path('employer_job_post_update/<int:id>/',employer_views.employer_job_post_update,name="employer_job_post_update"),
    path('employer_job_post_delete/<int:id>/',employer_views.employer_job_post_delete,name="employer_job_post_delete"),
    path('jobseeker_view_job_posts',jobseeker_views.jobseeker_view_job_posts,name="jobseeker_view_job_posts"),
    path('job_apply/<int:id>/',jobseeker_views.job_apply,name='job_apply'),
    path('jobseeker_view_my_job_applications',jobseeker_views.jobseeker_view_my_job_applications,name='jobseeker_view_my_job_applications'),
    path('employer_view_job_applications',employer_views.employer_view_job_applications,name="employer_view_job_applications"),
    path('employer_view_applicants_details/<int:id>/',employer_views.employer_view_applicants_details,name="employer_view_applicants_details")


]