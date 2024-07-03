from django.forms import ModelForm, Form, DateInput, SelectMultiple
from django.forms import TextInput, PasswordInput, CharField, EmailInput,Textarea,Select,CheckboxInput, FileInput
from django.core.validators import MinLengthValidator
from .models import *


class LoginForm(Form):
    username = CharField(
        max_length= 15,
        min_length= 4,
        required= True,
        label= 'Username',
        widget= TextInput({
            'class': 'form-control',
            'placeholder':'User Name'

        })

    )
    password = CharField(
        max_length= 15,
        min_length= 4,
        required= True,
        label= 'Password',
        widget= PasswordInput({
            'class': 'form-control',
            'placeholder':'Password'
        })

    )


class UserRegisterForm(ModelForm):

    confirm_password = CharField(
        max_length = 25,
        min_length = 8,
        required = True,
        validators = [
            MinLengthValidator(8, 'The password is too short.')
        ],
        widget = PasswordInput({
            'class': 'form-control',
            'placeholder':'Confirm Password'
        })
    )


    



    class Meta:
        model = User
        fields = [
           
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'phone',
            'dob',
            'short_bio',
            'job_title',
            'gender',
            'country',
            'open_to_hiring',
            'hobbies',
            'interest',
            'qualification',
            'multiple_images',
            'short_reel',
            'smoking_habit',
            'drinking_habit',
            'profile_photo',
            'age'


        ]
        widgets = {
            'username': TextInput({
                'class': 'form-control',
                'placeholder':'Username'
            }),

            'first_name': TextInput({
                'class': 'form-control'
            }),

            'last_name': TextInput({
                'class': 'form-control'
            }),

            'password': PasswordInput({
                'class': 'form-control',
                'placeholder':'Password'
            }),

            'email': EmailInput({
                'class': 'form-control',
                'placeholder':'email'
            }),

            'phone': TextInput({
                'class': 'form-control',
                'placeholder':'phone'
                 
            }),

            'dob': DateInput({
                'class': 'form-control',
                'placeholder':'YYYY-MM-DD'
            }),

            'short_bio': Textarea({
                'class': 'form-control',
                'rows': '3',
                'placeholder':'Short-Bio'
            }),

            'job_title': TextInput({
                'class': 'form-control'
            }),

            'gender': Select({
                'class': 'form-control'
            }),

            'country': Select({
                'class': 'form-control'
            }),
            'hobbies': Select({
                'class': 'form-control'
            }),
            'qualification': Select({
                'class': 'form-control'
            }),
            'interest': Select({
                'class': 'form-control'
            }),
            'age' : TextInput({
                'class': 'form-control',
                'placeholder':'Enter Age'
            })
           


        }

class JobSeekerForm(ModelForm):
      class Meta:
        model = JobSeeker
        fields = [
            'title',
            'expertise_level'
         ]
        widgets =  {
                     
            
                'title' : TextInput({
                    'class':'form-control',
                     'placeholder':'Title'
                    
                }),

                'expertise_level' : Select({
                    'class':'form-control',
                    
                })

            
        }



class EmployerForm(ModelForm):
      class Meta:
        model = Employer
        fields = [
            'company_name',
            'designation',
            'location'
         ]
        widgets =  {
                     
            
                'company_name' : TextInput({
                    'class':'form-control',
                     'placeholder':'Company Name'
                    
                }),

                'designation' : Select({
                    'class':'form-control',
                    
                }),
                'location' : Select({
                    'class':'form-control',
                    
                })

            
        }

class UserDetailesForm(ModelForm):


    class Meta:
        model = User
        fields = [
           
            'hobbies',
            'interest',
            'qualification',
            'multiple_images',
            'short_reel',
            'smoking_habit',
            'drinking_habit',
            'profile_photo',
            'age'


        ]
        widgets = {
            
            'dob': DateInput({
                'class': 'form-control',
                'placeholder':'YYYY-MM-DD'
            }),

            'hobbies': Select({
                'class': 'form-control'
            }),
            'qualification': Select({
                'class': 'form-control'
            }),
            'interest': Select({
                'class': 'form-control'
            }),
            'age' : TextInput({
                'class': 'form-control',
                'placeholder':'Enter Age'
            })
 

        }


















#user detailes  

# class UserDetailesForm(ModelForm):
#     class Meta:
#         model = UserActivity

#         exclude = ['user']
#         fields = [
           
#             'hobbies',
#             'interest',
#             'smoking_habit',
#             'drinking_habit',
#             'user_images',
#             'user_reels',
#             'user_qualification'

#         ]

#         widgets = {
#             'hobbies': Select({
#                 'class': 'form-control',
#                 'placeholder':'Choose'
#             }),
#             'interest': Select({
#                 'class': 'form-control',
#                 'placeholder':'Choose'
#             }),
#             'smoking_habit': Select({
#                 'class': 'form-control'
                
#             }),
#             'drinking_habit': Select({
#                 'class': 'form-control'
                
#             }),
#             'user_qualification': TextInput({
#                 'class': 'form-control',
#                 'placeholder':'Choose'
#             }),

#         }




