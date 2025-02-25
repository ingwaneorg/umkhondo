# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:course_id>/<int:user_id>/', views.task_list, name='task_list'),
]
