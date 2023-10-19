from django.utils import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

class Todo(models.Model):
    title = models.CharField(max_length=30)
    note = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_message_set')
    checked = models.BooleanField(default=False)
    
    def time_passed(self):
        return timezone.now() - self.created_at
    

    
   
    
