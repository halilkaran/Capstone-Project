from django.contrib import admin
from .models import Blog, Comment, Like, BlogView
# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(BlogView)