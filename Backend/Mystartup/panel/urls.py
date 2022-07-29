from django.contrib import admin
from django.urls import path,include
from . import views as panelviews

urlpatterns = [
    path('home/',panelviews.login,name="home"),
    path('dashboard/',panelviews.register,name="dashboard"),
]