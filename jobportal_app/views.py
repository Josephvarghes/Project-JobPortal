from django.shortcuts import render

def login_view(request):
    return render(request, 'authentication/login.html')

def signup_view(request):
    return render(request, 'authentication/signup.html')

def forgot_password_view(request):
    return render(request, 'authentication/forgot_password.html')

def home_view(request):
    return render(request, 'authentication/home.html')


def profile_view(request):
    return render(request, 'accounts/work.html')


