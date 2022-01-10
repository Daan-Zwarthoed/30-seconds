from . import views
from django.urls import path

urlpatterns = [
    path('', views.loginUser, name='loginUser'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),
]
