from django.urls import path
from .views import *

app_name = 'accounts'


urlpatterns = [
   

    path('', loginView.as_view(), name='login'),

    path('signup/', signupView.as_view(), name='signup'),

    path('logout/', logoutView.as_view(), name='logout'),

    path('forgot/', forgotView.as_view(), name='forgot_password'),

    path('profile/', RegisterView.as_view(), name='profile'),

    path('address/', addressView.as_view(), name = 'address'),

    path('detailes/', userDetailesView.as_view(), name = 'userdetailes'),

    path('detailes/user-selection', userSelectionView.as_view(), name = 'userselection'),

    path('detailes/user-selection/jobseeker', jobSeekerView.as_view(), name = 'jobseeker'),


    path('detailes/user-selection/employer', employerView.as_view(), name = 'employer'),

    path('employer/', employerLandingView.as_view(), name = 'employerlanding'),


    path('home/', userLandingView.as_view(), name = 'userlanding'),

    path('home/jobseeker', jsHomeView.as_view(), name = 'jshome'),

    path('home/post-job', jobPostView.as_view(), name = 'jobpost'),

    path('home/posted-jobdetailes', EmployerPostedJobView.as_view(), name = 'postedjobdetailes')


    
    
  
]