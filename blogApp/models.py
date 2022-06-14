from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    OPTIONS = (
        ("d", "Draft"),
        ("p", "Published")
    )
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=500)
    image = models.URLField(default="https://kigsmtua.github.io/assets/img/django.png")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)      
    status = models.CharField(max_length=10, choices=OPTIONS, default="d")
    slug = models.SlugField(blank=True)         #* django-is-perfekt

    def __str__(self):
        return self.title      
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def view_count(self):
        return self.blogview_set.all().count()
    
    def like_count(self):
        return self.like_set.all().count()
    
    def comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class BlogView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username