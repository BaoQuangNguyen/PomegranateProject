from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks_index, name='index'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('timer/', views.timer, name='timer'),
    path('breaktimer/', views.break_timer, name='breaktimer'),
    path('completedtask/<int:task_id>/', views.completed_task_detail, name='completed_task_detail'),
    path('tasks/<int:task_id>/mark_completed/', views.mark_task_completed, name='mark_completed'),
    path('tasks/chart/', views.TaskChartView.as_view(), name='task_chart_view'),

]
