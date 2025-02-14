from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('preorder/', views.preorder, name='preorder'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
]