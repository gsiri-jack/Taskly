from django.db import models
from datetime import datetime

# Create your models here.

status_choices = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('in_progress', 'In Progress'),
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
