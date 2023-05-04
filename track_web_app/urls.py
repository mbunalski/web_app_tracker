from django.urls import path

from . import views

app_name = 'track_web_app'
urlpatterns = [
    path('', views.index, name='index'),
]