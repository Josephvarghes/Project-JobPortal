from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.location

class Designation(models.Model):
    designation = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.designation



class Hobbies(models.Model):
    Hobbie = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.Hobbie


class Interest(models.Model):
    interest = models.CharField(max_length=100)
    def __str__(self):
        return self.interest
    

class Qualification(models.Model):
    qualification = models.CharField(max_length=100)
    def __str__(self):
        return self.qualification
    

class MultipleImages(models.Model):
    images = models.FileField(upload_to='multiple_images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.images
    

class ShortReels(models.Model):
    short_reel = models.FileField(upload_to='shortreels/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.short_reel
    
    

    

    
class User(AbstractUser):
   
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    COUNTRY_CHOICES= (
        ('IN', 'India'),
    )

    QUALIFICATION_CHOICES = (
        ('H', 'High School'),
        ('D', 'Diploma'),
        ('U', 'Undergraduate'),
        ('G', 'Graduate'),
        ('P', 'Postgraduate'),
        ('Ph', 'PhD'),
        ('O', 'Other'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    short_bio = models.TextField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=50, default='IN', choices=COUNTRY_CHOICES,  blank=True, null=True)
    open_to_hiring = models.BooleanField(default=False)
    

    hobbies = models.ManyToManyField(Hobbies, related_name="user_hobbies")
    interest = models.ManyToManyField(Interest, related_name="user_interest")
    qualification = models.ManyToManyField(Qualification,  related_name="user_qualification" )
    multiple_images = models.ManyToManyField(MultipleImages,  related_name="user_images",  blank=True, null=True)
    short_reel =  models.ManyToManyField(ShortReels, related_name="user_reels",  blank=True, null=True)
    smoking_habit = models.BooleanField(default=False)
    drinking_habit = models.BooleanField(default=False)
    age = models.CharField(max_length=15, blank=True, null=True)


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
    



class JobSeeker(models.Model):
    
    LEVEL_CHOICE = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('E', 'Expert')
    )


    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    expertise_level = models.CharField(max_length=100, default='B', choices = LEVEL_CHOICE)

    def __str__(self):
        return self.title






class Employer(models.Model):
    
#    DESIGNATION_CHOICES = (
#     ('IN', 'Intern'),
#     ('JD', 'Junior Developer'),
#     ('SD', 'Senior Developer'),
#     ('TL', 'Team Lead'),
#     ('MG', 'Manager'),
#     ('DR', 'Director'),
#     ('CEO', 'Chief Executive Officer'),
#    )
    
   
#    LOCATION_CHOICES = (
#     ('MUM', 'Mumbai'),
#     ('DEL', 'Delhi'),
#     ('BLR', 'Bangalore'),
#     ('HYD', 'Hyderabad'),
#     ('CHE', 'Chennai'),
#     ('KOL', 'Kolkata'),
#     ('PUN', 'Pune'),
#     ('JAI', 'Jaipur'),
#     ('KOC', 'Kochi'),
#     ('AMD', 'Ahmedabad'),
#    )

   id = models.BigAutoField(primary_key=True)

   user = models.ForeignKey(User, on_delete=models.CASCADE)
   designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

   company_name = models.TextField(max_length=100)
   location = models.ForeignKey(Location, on_delete=models.CASCADE)


   def __str__(self):
        return self.company_name









class UserHobbies(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hobbies = models.ForeignKey(Hobbies,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'hobbies')


class UserInterest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'interest')


class UserQualification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qualification = models.ForeignKey(Interest,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'qualification')




