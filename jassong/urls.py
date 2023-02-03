from django.urls import path
from  . import views

app_name = 'jassong'

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources, name='resources'),
    path('post/', views.newsFeed, name='post'),
    path('donation/', views.donation, name='donation'),
    path('mosque/', views.mosque, name='mosque'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

