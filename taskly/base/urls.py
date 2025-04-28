from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('tsk/<int:id>', views.task_detail, name='task_detail'),
    path('create_task', views.create_task, name='create_task'),
]
