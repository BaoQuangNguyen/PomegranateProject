from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasklist/', views.tasks_index, name='index'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('tasks/<int:task_id>/update_status/', views.update_status, name='update_status'),
    path('timer/', views.timer, name='timer'),
    path('tasks/<int:task_id>/results/', views.task_results, name='task_results'),
    path('breaktimer/', views.break_timer, name='breaktimer'),
]