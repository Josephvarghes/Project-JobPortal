from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, View
from django.urls import reverse_lazy

# Create your views here.


class jobCreate(CreateView):
    # model = 
    # form_class = 
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        form.instance.company_name = self.request.user.company_name
        return super().form_valid(form)

