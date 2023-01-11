from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import HttpResponse
# Create your views here.

class StartView(TemplateView):
    template_name = 'protect/protect.html'



