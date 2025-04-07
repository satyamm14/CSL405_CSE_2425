
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('accounts/login/', views.login_view, name="login"),
]
