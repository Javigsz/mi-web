from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
class ListView(ListView):
    model = Project
    template_name = "portfolio/portfolio_list.html"
    #si no defines template_name, usa uno llamado en este caso "page_list.html"
    #si no defines el nombre del objeto que tienes que recorrer en page_list.html, usa object_list o "modelo"_list

class DetailView(DetailView):
    model = Project
    template_name = "portfolio/portfolio_detail.html"
    #si no defines template_name, usa uno llamado en este caso "page_detail.html"
    #si no defines el nombre del objeto que tienes que acceder en page_detail.html, usa object o "modelo"

    def get_object(self):
        return get_object_or_404(Project, title = self.kwargs['title'])