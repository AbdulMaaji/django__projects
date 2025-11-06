from django.urls import path
from . import views


urlpatterns = [
    path('todo/', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
