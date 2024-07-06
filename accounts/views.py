from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views import View
from django.views.generic import CreateView,  View


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
                return redirect("accounts:userdetailes")
            else:
                return HttpResponse('Invalid username or password')
        #form is not valid then..
        return render(request, self.template_name, {'form': form} )

  
 

class signupView(LoginRequiredMixin, View):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    template_login = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
         return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(data = request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        #form is valid then..
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        login(request, user)
        return redirect(reverse('accounts:userdetailes'))

   

   

        
    


# class forgotView(View):

#     def __init__(self)
   




#for profile
class RegisterView(LoginRequiredMixin, View):
       
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

class userDetailesView(LoginRequiredMixin, View):
    form_class = UserDetailesForm
    template_name = 'accounts/userdetailes.html'
    

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        
        user = self.request.user
        
        hobbies = form.cleaned_data['hobbies']
        interest = form.cleaned_data['interest']
        user.drinking_habit = form.cleaned_data['drinking_habit']
        qualification = form.cleaned_data['qualification']
        multiple_images = form.cleaned_data['multiple_images']
        short_reel = form.cleaned_data['short_reel']
        user.smoking_habit = form.cleaned_data['smoking_habit']
        user.age = form.cleaned_data['age']
        if 'profile_photo' in form.cleaned_data:
            user.profile_photo = form.cleaned_data['profile_photo']
            user.save()
            #for saving many to many field
        user.hobbies.set(hobbies)
        user.interest.set(interest)
        user.qualification.set(qualification)
        user.multiple_images.set(multiple_images)
        user.short_reel.set(short_reel)
        
        return redirect(reverse('accounts:userselection'))




    # def get(self, request):
    #      return render(request, self.template_name, {'form': self.form_class()})
    
    # def post(self, request):
    #     form = self.form_class(data = request.POST)
    #     if not form.is_valid():
    #         return render(request, self.template_name, {'form': form})
    #     #form is valid then..
    #     user_details = form.save(commit=False)
    #     user_details.user = request.user  
    #     user_details.save()
        
    #     return redirect('accounts:userselection')
    
    
 

class userSelectionView(LoginRequiredMixin, View):
     template_name = 'accounts/user_selection.html'

     def get(self, request, *args, **kwargs):
        return render(request, self.template_name )


#for jobseeker page
class jobSeekerView( View):

    form_class = JobSeekerForm
    template_name = 'accounts/jobseeker.html'
    

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        
        form.save()
 
        return redirect(reverse('accounts:userlanding'))







class employerView(LoginRequiredMixin, View):

    form_class = EmployerForm
    template_name = 'accounts/employer.html'
    

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        
        user = self.request.user
        
        user.company_name = form.cleaned_data['company_name']
        user.designation = form.cleaned_data['expertise_level']
        user.location = form.cleaned_data['location']
    
        user.save()

        return redirect(reverse('accounts:userlanding'))



class userLandingView(View):
    template_name = 'accounts/userlandingpage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class jobPostView(View):
   
    template_name = 'accounts/postjob.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
