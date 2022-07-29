from django.contrib import admin
from django.urls import path,include
from . import views as accountsviews

urlpatterns = [
    path('login/',accountsviews.login,name="login"),
    path('register/',accountsviews.register,name="login"),
]