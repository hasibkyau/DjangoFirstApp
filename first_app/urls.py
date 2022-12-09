# from django.conf.urls import url
from django.urls import re_path as url
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form')
]
