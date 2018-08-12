from django.conf.urls import url
from django.urls import path, include

from myFlix.webapp import views

urlpatterns = [
    path('', views.index, name='index'),
]