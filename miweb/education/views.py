from django.views.generic.list import ListView
from .models import Language

# Create your views here.
# Create your views here.
class ListView(ListView):
    model = Language
    template_name = "education/education_list.html"
    #si no defines template_name, usa uno llamado en este caso "page_list.html"
    #si no defines el nombre del objeto que tienes que recorrer en page_list.html, usa object_list o "modelo"_list