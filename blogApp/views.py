from django.shortcuts import render
from rest_framework import generics
from blogApp.models import Blog
from blogApp.serializer import BlogSerializer
from rest_framework.viewsets import ModelViewSet

# class BlogList(generics.ListAPIView):
#     serializer_class=BlogSerializer
#     queryset = Blog.objects.all()

class BlogCRUD(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer