from django.urls import path
from app1.views import index, turma

urlpatterns = [
    path('', index),
    path('turma', turma)
]