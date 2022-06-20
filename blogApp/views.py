from rest_framework import generics
from blogApp.permissions import IsOwnerOrReadOnly
from .models import Blog, Comment
from .serializer import BlogSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
# class BlogList(generics.ListAPIView):
#     serializer_class=BlogSerializer
#     queryset = Blog.objects.all()
class BlogCRUD(ModelViewSet):
    # permission_classes = [IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer
    def get_permissions(self):
        if self.action == 'list' or self.action == "create":
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
class CommentCRUD(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = CommentSerializer