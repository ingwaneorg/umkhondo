# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_code>/<int:user_id>/', views.task_list, name='task_list'),
]
