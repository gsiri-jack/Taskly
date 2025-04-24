from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('tsk/<int:id>', views.task_detail, name='task_detail'),
]
