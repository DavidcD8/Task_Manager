from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Task list view
    path('create/', views.task_create, name='task_create'),  # Task create view
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('toggle-completed/<int:pk>/', views.task_toggle_completed, name='task_toggle_completed'),
]
