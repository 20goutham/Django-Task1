from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Hai',views.hello_world),
    path('task/', views.task_view)
]
