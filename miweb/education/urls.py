from .views import ListView
from django.urls import path

urlpatterns = [
    path('',ListView.as_view(), name="education_list"),
]