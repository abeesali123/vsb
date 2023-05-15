from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about', views.contact, name='about'),
        path('services', views.contact, name='service'),
        path('projects', views.contact, name='projects'),
        path('contact', views.contact, name='contact'),
]