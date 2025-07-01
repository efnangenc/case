from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.post import Post
from ..serializers.post import PostSerializer
from ..serializers.comment import CommentSerializer  # unutma import

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()  # related_name='comments' olmalı Post modelinde
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
