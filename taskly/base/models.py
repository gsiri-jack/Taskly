from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

status_choices = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('in_progress', 'In Progress'),
]
priority_choices = [
    ('normal', 'Normal'),
    ('medium', 'medium'),
    ('high', 'high'),
]


class sample(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=datetime.now)  # Pass callable here
    status = models.CharField(
        max_length=20, choices=status_choices, default='in_progress')

    def __str__(self):
        return self.title


class tag(models.Model):
    tag_name = models.CharField(max_length=50, default='genral')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)


class task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(default=datetime.now)
    due_date = models.DateField(default=datetime.now)
    priority = models.CharField(
        max_length=20, choices=priority_choices, default='normal')
    status = models.CharField(
        max_length=20, choices=status_choices, default='in_progress')
    tags = models.ManyToManyField(tag)


class task_tag_link(models.Model):
    task_id = models.ForeignKey(task, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(tag, on_delete=models.CASCADE)
