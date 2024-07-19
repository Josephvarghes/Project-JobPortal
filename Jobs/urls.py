from django.urls import path
from .views import *

app_name = 'jobs'

urlpatterns = [
    path('',jobCreateView.as_view(), name = 'job_create'),

   
]