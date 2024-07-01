from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.
from django.views import View


class loginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    template_user = 'accounts/userdetailes.html'
    form_class1 = UserRegisterForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class()})
   
    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, self.template_user, {'form': self.form_class1()})
            else:
                return HttpResponse('Invalid username or password')
        #form is not valid then..
        return render(request, self.template_name, {'form': form} )

  
 

class signupView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    template_login = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
         return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request, *args, **kwargs):
        form = self.class_name(data = request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        #form is valid then..
        user = form.save(commit=False)
        user.password = form.cleaned_data['password']
        user.save()
        return render(request, self.template_login)

   

   

        
    


# class forgotView(View):

#     def __init__(self)
   




#for profile
class RegisterView(View):
       
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':  self.form_class()})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        
        #form is valid then
        user = form.save(commit=False)
        user.password = form.cleaned_data['password']
        user.save()
        return HttpResponse("successfully entered profile detail")



#for address creation

class addressView(View):
    template_name = 'accounts/address_create.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    


#for userdetailes(2nd page)

class userDetailesView(View):
    # form_class = UserRegisterForm
    template_name = 'accounts/userdetailes.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
 

class userSelectionView(View):
     template_name = 'accounts/user_selection.html'

     def get(self, request, *args, **kwargs):
        return render(request, self.template_name )
     

class jobSeekerView(View):
     template_name = 'accounts/jobseeker.html'
     form_class = UserRegisterForm

     def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class()})
     


class employerView(View):
     template_name = 'accounts/employer.html'
     form_class = UserRegisterForm

     def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class()})





     