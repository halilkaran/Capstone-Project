from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    # get_comment_count = serializers.ReadOnlyField(source="comment_count")
    # get_like_count = serializers.ReadOnlyField(source="like_count")
    # get_view_count = serializers.ReadOnlyField(source="view_count")

    class Meta:
        model = Blog
        fields = (
        "id",
        "title", 
        "content", 
        "image", 
        "publish_date",
        "last_update", 
        "author", 
        "status",
        "slug",
        "comment_count", 
        "view_count",         
        "like_count",
        )
