from django.urls import path
from .views import home_page

urlpatterns: list = [
    path('', home_page)
]