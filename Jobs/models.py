from django.db import models
from accounts.models import Employer
# Create your models here.

class Jobtitle(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.title


class Jobpost(models.Model):

    JOB_TYPES = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship')
    )

    SALARY_TYPES = (
        ('Month','Month'),
        ('Year', 'Year')
    )

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_title = models.ForeignKey(Jobtitle, on_delete=models.CASCADE)
    description = models.TextField()
    company_name = models.CharField(max_length=200, null=True, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField(auto_now_add=True)
    job_mode = models.CharField(max_length=100, choices=JOB_TYPES, default='FT')
    vacancies = models.PositiveIntegerField()
    salary_type = models.CharField(max_length=255, choices=SALARY_TYPES, default='mnt' )
    location = models.CharField(max_length=255, null=True, blank=True)

