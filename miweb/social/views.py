from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Link

# Create your views here.
class ListView(ListView):
    model = Link
    template_name = "social/social_list.html"
    