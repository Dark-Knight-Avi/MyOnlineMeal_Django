from django.contrib import admin
from django.urls import path
from mealApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("home/", views.index, name='home'),
    # path('/services', views.services, name='services'),
]
admin.site.site_header = "MyOnlineMeal Admin"
admin.site.site_title = "MyOnlineMeal Admin Portal"
admin.site.index_title = "Welcome to MyOnlineMeal Portal"