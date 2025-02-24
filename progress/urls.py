# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_num>/<int:user_id>/', views.task_list, name='task_list'),
]
