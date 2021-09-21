from django.contrib import admin
from django.urls import path
from .views import home, logoutHome

urlpatterns = [
    path('', home, name="home"),
    path('home', logoutHome, name="logoutHome")

]