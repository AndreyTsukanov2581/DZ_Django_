from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectsListView.as_view(), name='projects_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
]