from django.urls import path
from .views import home, galery, contact

urlpatterns = [
    path('', home, name="home"),
    path('galery/', galery, name="galery"),
    path('contact/', contact, name="contact"),
]