from django.urls import path
from .views import get_data

urlpatterns = [
    path ('users/', get_data, name="get_data")
]
