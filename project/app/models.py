from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.created_date = timezone.now()
        self.save()
    
    def end_date(self):
        deadline = self.deadline
        today = timezone.now()
        d_day = (deadline - today).days
        return d_day