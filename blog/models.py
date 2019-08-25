from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class Post(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    article = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)

class Category(models.Model):
    category = models.CharField(max_length=20)

class Feelings(models.Model):
    feelings_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    textarea = models.TextField()
    time = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    blog = models.ForeignKey('Post',on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    comment_time = models.DateTimeField()
    comment_content = models.TextField()


class Word(models.Model):
    content = models.TextField()
    add_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.add_time.strftime('%Y-%m-%d')
