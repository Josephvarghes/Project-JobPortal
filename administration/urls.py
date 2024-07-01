from django.urls import path
from . import views



urlpatterns = [

    path('', views.adminDashboard, name='dashboard'),
    path('company/', views.companyList, name='company'),
    path('users/', views.usersList, name='users'),
    path('notifications/', views.notifications, name='notifications'),
    path('sign-in/', views.adminSignin, name='sign-in'),
    path('sign-up/', views.adminSignup, name='sign-up'),
    path('profile/', views.profile, name='profile'),
          
   
    
]