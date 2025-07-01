from rest_framework import serializers
from ..models.comment import Comment

class CommentSerializer(serializers.ModelSerializer):
    postId = serializers.PrimaryKeyRelatedField(source='post', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'postId', 'name', 'email', 'body']
