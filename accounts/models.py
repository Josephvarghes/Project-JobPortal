from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    COUNTRY_CHOICES= (
        ('IN', 'India'),
    )
    

    INTEREST_CHOICES = (
        ('P', 'Programming'),
        ('R', 'Reading'),
        ('L', 'Learning tech'),
    )

    HOBBIES_CHOICES = (
        ('G', 'Gamming'),
        ('S', 'Singing'),
        ('V', 'Video editing'),
    )


    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    short_bio = models.TextField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES)
    country = models.CharField(max_length=50, default='IN', choices=COUNTRY_CHOICES)
    open_to_hiring = models.BooleanField(default=False)
    hobbies = models.CharField(max_length=100, default='G', choices=HOBBIES_CHOICES)
    interest = models.CharField(max_length=100, default='P', choices=INTEREST_CHOICES)
    qualification = models.CharField(max_length=15, blank=True, null=True)
    multiple_images = models.ImageField(upload_to='multiple_images/', blank=True, null=True)
    short_reel = models.FileField(upload_to='shortreels/', blank=True, null=True)

class Address(models.Model):
    COUNTRY_CHOICES= (
        ('IN', 'India'),
    )
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    address_line_1 = models.TextField(max_length=250)
    address_line_2 = models.TextField(max_length=250)
    address_line_3 = models.TextField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='IN', choices=COUNTRY_CHOICES)
    pincode = models.CharField(max_length=25)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_default = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'name']

    def __str__(self):
        return f'''{self.address_line_1}
        {self.address_line_2}
        {self.address_line_3}'''