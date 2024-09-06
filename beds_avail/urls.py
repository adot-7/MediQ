from django.urls import path
from . import views

app_name = 'beds_avail'
urlpatterns = [
    path('', views.home, name='beds_avail_home')
]

