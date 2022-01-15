from django.urls import path
from encuestas import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('realizar-encuesta/', views.CreateEncuesta.as_view(), name='create-encuesta'),
]