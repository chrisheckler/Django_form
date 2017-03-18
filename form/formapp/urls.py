
from django.conf.urls import url 
from django.contrib import admin
from form import views

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
]
