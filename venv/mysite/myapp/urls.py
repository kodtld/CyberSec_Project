from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('home/', views.index, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('create_game/', views.createGame, name='create_game'),
    path('update_game/<str:pk>/', views.updateGame, name='update_game'),
    path('delete_game/<str:pk>/', views.deleteGame, name='delete_game')
]
