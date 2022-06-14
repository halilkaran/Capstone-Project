from django.shortcuts import render
from rest_framework import generics
from blogApp.models import Blog
from blogApp.serializer import BlogSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly

# class BlogList(generics.ListAPIView):
#     serializer_class=BlogSerializer
#     queryset = Blog.objects.all()

class BlogCRUD(ModelViewSet):
    permission_classes=[IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer