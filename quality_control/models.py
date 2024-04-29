from django.db import models
from tasks.models import Task
from tasks.models import Project

class BugReport(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in progress', 'В работе'),
        ('finished', 'Завершена'),
    )
    PRIORITY_CHOICES = (
        ('5', 'Наивысший приоритет'),
        ('4', 'Высокий приоритет'),
        ('3', 'Нормальный приоритет'),
        ('2', 'Низкий приоритет'),
        ('1', 'Наименьший приоритет'),
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Task,
        on_delete = models.CASCADE
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='3',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class FeatureRequest(models.Model):
    STATUS_CHOICES = (
        ('under review', 'Рассмотрение'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    )
    PRIORITY_CHOICES = (
        ('5', 'Наивысший приоритет'),
        ('4', 'Высокий приоритет'),
        ('3', 'Нормальный приоритет'),
        ('2', 'Низкий приоритет'),
        ('1', 'Наименьший приоритет'),
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='under review',
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='3',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
