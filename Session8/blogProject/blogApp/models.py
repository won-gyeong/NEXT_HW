from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(null=True, max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 
def __str__(self):
    return self.title