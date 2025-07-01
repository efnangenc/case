from rest_framework import serializers
from ..models.post import Post
from ..serializers.comment import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'userId', 'title', 'body', 'comments']