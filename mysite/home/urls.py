from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('newGroup', views.newGroup, name='newGroup'),
    path('group', views.group, name='group'),
]
