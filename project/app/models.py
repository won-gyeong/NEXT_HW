from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateField(null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.created_date = timezone.now()
        self.save()
    
    def end_date(self):
        deadline = self.deadline
        today = date.today()
        d_day = (deadline - today).days
        return d_day
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    
    def __str__(self):
        return self.content
    
class Recomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, db_constraint=False, related_name='recomments')
    content = models.TextField(default='')

    def __str__(self):
        return self.content
    

    