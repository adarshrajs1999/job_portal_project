from django.urls import path

from job_portal_app import views

urlpatterns = [
    path('', views.home, name='home')

]