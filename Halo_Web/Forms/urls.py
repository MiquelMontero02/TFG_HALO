from django.urls import path
from . import views

urlpatterns = [
    path('Forms/', views.forms, name='Forms'),
]