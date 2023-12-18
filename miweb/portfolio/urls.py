from .views import DetailView,ListView
from django.urls import path

urlpatterns = [
    path('',ListView.as_view(), name="portfolio_list"),
    path('<title>', DetailView.as_view(), name="portfolio_detail"),
]