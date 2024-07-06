from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Hobbies)
admin.site.register(Interest)
admin.site.register(Qualification)
admin.site.register(JobSeeker)
admin.site.register(Employer)

