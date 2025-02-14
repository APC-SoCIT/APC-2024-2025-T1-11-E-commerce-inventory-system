from django.urls import path
from .views import register, login_view, logout_view
from django.shortcuts import render
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('loginfailed/', lambda request: render(request, 'accounts/login_failed.html'), name='loginfailed'),
]
