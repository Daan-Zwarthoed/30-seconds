from . import views
from django.urls import path

urlpatterns = [
    path('', views.settings, name='settings'),
    path('playing', views.playing, name='playing'),
]
