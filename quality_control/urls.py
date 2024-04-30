from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bug_list_url, name='bug_list'),
    path('features/', views.improvements_req_url, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_id_detail, name='feature_id_detail'),
]