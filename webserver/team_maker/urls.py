from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faceit_input', views.faceit_input, name='faceit_input')
]