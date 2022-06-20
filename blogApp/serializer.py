from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer) :    
    class Meta :
        model = Comment
        fields = ('id', "user", "blog", "time_stamp", "content")

class BlogSerializer(serializers.ModelSerializer):
    # get_comment_count = serializers.ReadOnlyField(source="comment_count")
    # get_like_count = serializers.ReadOnlyField(source="like_count")
    # get_view_count = serializers.ReadOnlyField(source="view_count")
    # get_comments = serializers.ReadOnlyField(source="comments")


    

    comment_set= serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name = 'comment-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Blog
        fields = (
        "comment_set",       
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