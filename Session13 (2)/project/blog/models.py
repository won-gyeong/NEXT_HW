from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="TITLE")
    content = models.TextField()
    deadline = models.DateField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-create_dt', 'author')

    def __str__(self):
        return f'{self.title} - {self.author}'
    
    def get_absolute_url(self):
        return reverse(f'blog:post_detail', args=[self.id])
    
    def get_previous(self):
        return self.get_previous_by_create_dt()
    
    def get_next(self):
        return self.get_next_by_create_dt()

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    create_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_dt', 'post', 'author')

    def __str__(self):
        return f'{self.title} - {self.author}'
    
class Recomment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='recomments')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomments')
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recomments')


    def __str__(self):
        return self.title
    

    