from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout', views.logut_user, name='logout'),
    path('register', views.register_user, name='register'),
    # path('register/login', views.register_user, name='register_login')
]
