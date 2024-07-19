from .models import *
from django.forms import TextInput, ModelForm


class JobPostForm(ModelForm):
    class Meta:
        model = Jobpost
        fields = [
            ''
        ]

        widget = {

        }