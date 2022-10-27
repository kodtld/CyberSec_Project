from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('home/', views.index, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register')
]