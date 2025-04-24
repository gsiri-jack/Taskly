from django.db import models

# Create your models here.

status_choices = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('in_progress', 'In Progress'),]


class sample(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=status_choices, default='in_progress')

    def __str__(self):
        return self.title
