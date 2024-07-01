from django.shortcuts import render

# Create your views here.


def adminDashboard(request):
    return render(request, 'administration/dashboard.html')


def companyList(request):
    return render(request, 'administration/company.html')


def usersList(request):
    return render(request, 'administration/users.html' )


def notifications(request):
    return render(request, 'administration/notifications.html' )


def adminSignin(request):
    return render(request, 'administration/sign-in.html' )


def adminSignup(request):
    return render(request, 'administration/sign-up.html' )


def profile(request):
    return render(request, 'administration/profile.html' )

