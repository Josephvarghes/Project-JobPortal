from django.forms import ModelForm, Form, ModelChoiceField
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
            'profile_photo',
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
            'short_reel'

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

            'dob': TextInput({
                'class': 'form-control',
                'placeholder':'MM/DD/YY'
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

            'open_to_hiring': CheckboxInput(),

            'profile_photo': FileInput({
                'class': 'form-control',
                'placeholder':'upload resume'
            }),

            'qualification' :  TextInput({
                'class': 'form-control'

            }),

            'multiple_images' :  FileInput({
                'class': 'form-control',
                'placeholder':'Other pictures upload here'
            }),

            'interest': Select({
                'class': 'form-control'
            }),

            'hobbies': Select({
                'class': 'form-control'
            }),

           'short_reel': FileInput({
                'class': 'form-control',
                'placeholder':'upload your reel video'
            })


            

        }
    

# class ShortReelUploadForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['title', 'video']
    
#     def clean_video(self):
#         allowed_types = ["video/mp4", "video/avi", "video/mov"]
#         max_size = 1024 * 1024 * 100  # 100 MB
#         return self.clean_file('video', allowed_types, max_size)

