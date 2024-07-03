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
        ('T', 'Technology'),
        ('S', 'Science'),
        ('L', 'Literature'),
        ('T', 'Travel'),
        ('F', 'Food'),
        ('H', 'Health'),
        ('Fi', 'Fitness'),
        ('E', 'Education'),
        ('Fa', 'Fashion'),
        ('En', 'Entertainment'),
        ('Fin', 'Finance'),
        ('P', 'Politics'),
        ('Env', 'Environment'),
        ('Sp', 'Sports'),
        ('Hi', 'History'),
    )
    
    HOBBY_CHOICES = (
        ('R', 'Reading'),
        ('T', 'Traveling'),
        ('C', 'Cooking'),
        ('S', 'Sports'),
        ('G', 'Gardening'),
        ('Ga', 'Gaming'),
        ('F', 'Fitness'),
        ('P', 'Photography'),
        ('W', 'Writing'),
        ('D', 'Dancing'),
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
    

    hobbies = models.CharField(max_length=100, default='R', choices=HOBBY_CHOICES,  blank=True, null=True)
    interest = models.CharField(max_length=100, default='T', choices=INTEREST_CHOICES,  blank=True, null=True)
    qualification = models.CharField(max_length=100, default='H', choices=QUALIFICATION_CHOICES,  blank=True, null=True)
    multiple_images = models.ImageField(upload_to='multiple_images/', blank=True, null=True)
    short_reel = models.FileField(upload_to='shortreels/', blank=True, null=True)
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
    

    title = models.TextField(max_length=100)
    expertise_level = models.CharField(max_length=100, default='B', choices = LEVEL_CHOICE)


class Employer(models.Model):
    
   DESIGNATION_CHOICES = (
    ('IN', 'Intern'),
    ('JD', 'Junior Developer'),
    ('SD', 'Senior Developer'),
    ('TL', 'Team Lead'),
    ('MG', 'Manager'),
    ('DR', 'Director'),
    ('CEO', 'Chief Executive Officer'),
   )
    
   
   LOCATION_CHOICES = (
    ('MUM', 'Mumbai'),
    ('DEL', 'Delhi'),
    ('BLR', 'Bangalore'),
    ('HYD', 'Hyderabad'),
    ('CHE', 'Chennai'),
    ('KOL', 'Kolkata'),
    ('PUN', 'Pune'),
    ('JAI', 'Jaipur'),
    ('KOC', 'Kochi'),
    ('AMD', 'Ahmedabad'),
   )



   company_name = models.TextField(max_length=100)
   designation = models.CharField(max_length=100, default='IN', choices = DESIGNATION_CHOICES )
   location = models.CharField(max_length=100, default='KOC', choices = LOCATION_CHOICES  )



# class Interest(models.Model):          

#     INTEREST_CHOICES = (
#         ('Technology', 'Technology'),
#         ('Science', 'Science'),
#         ('Literature', 'Literature'),
#         ('Travel', 'Travel'),
#         ('Food', 'Food'),
#         ('Health', 'Health'),
#         ('Fitness', 'Fitness'),
#         ('Education', 'Education'),
#         ('Fashion', 'Fashion'),
#         ('Entertainment', 'Entertainment'),
#         ('Finance', 'Finance'),
#         ('Politics', 'Politics'),
#         ('Environment', 'Environment'),
#         ('Sports', 'Sports'),
#         ('History', 'History'),
#     )
    
#     user_interest = models.CharField(max_length=50, default='Technology', choices=INTEREST_CHOICES)
   
#     def __str__(self):
#         return str(self.user_interest)
    





# class Hobby(models.Model):    

#     HOBBY_CHOICES = (
#         ('Reading', 'Reading'),
#         ('Traveling', 'Traveling'),
#         ('Cooking', 'Cooking'),
#         ('Sports', 'Sports'),
#         ('Gardening', 'Gardening'),
#         ('Gaming', 'Gaming'),
#         ('Fitness', 'Fitness'),
#         ('Photography', 'Photography'),
#         ('Writing', 'Writing'),
#         ('Dancing', 'Dancing'),
#     )

#     user_hooby = models.CharField(max_length=100, choices=HOBBY_CHOICES)

#     def __str__(self):
#         return str(self.user_hooby)



  
# class UserImages(models.Model):
    
#     image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    

#     def __str__(self):
#         return str(self.image)
    
    

# class UserShortReels(models.Model):

#     reel = models.FileField(upload_to='short_reels/', blank=True, null=True)
    

#     def __str__(self):
#         return str(self.reel)




# class UserQualifications(models.Model):
#     LEVEL_CHOICES = (
#         ('High School', 'High School'),
#         ('Diploma', 'Diploma'),
#         ('Undergraduate', 'Undergraduate'),
#         ('Graduate', 'Graduate'),
#         ('Postgraduate', 'Postgraduate'),
#         ('PhD', 'PhD'),
#         ('Other', 'Other'),
#     )
    
    

#     name = models.CharField(max_length=100, choices=LEVEL_CHOICES, unique=True)

#     def __str__(self):
#         return self.name


# class UserActivity(models.Model):
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     hobbies = models.ManyToManyField(Hobby)
#     interest = models.ManyToManyField(Interest, related_name='user_interest')
#     smoking_habit = models.BooleanField(default=False)
#     drinking_habit = models.BooleanField(default=False)
#     user_images = models.ForeignKey(UserImages, related_name='user_image', on_delete=models.CASCADE)
#     user_reels  = models.ForeignKey(UserShortReels, related_name='user_reels', on_delete=models.CASCADE)
#     user_qualification = models.ManyToManyField(UserQualifications, related_name='user_qualification')
     


#     def __str__(self):
#         return self.user.username