from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


GENDER_CHOICE = (
    ('F' ,  'Female'),
    ('M' , 'Male'),
)

GENDER_CHOICE = (
    ('IN' ,  'India'),
 
)

phone = models.CharField(max_length=15, blank=True, null=True)
profile_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
