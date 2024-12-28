from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Task list view
    path('create/', views.task_create, name='task_create'),  # Task create view
    path('update/<int:pk>/', views.task_update, name='task_update'),

]
