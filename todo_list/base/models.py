from django.db import models
import uuid
from enums import Status, Priority
from django.contrib.auth.models import User


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=[(tag.name, tag.value) for tag in Status], default='Pending')
    priority = models.CharField(max_length=30, choices=[(tag.name, tag.value) for tag in Priority], default='Low')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['status']