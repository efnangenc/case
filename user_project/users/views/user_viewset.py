from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.user import User
from ..serializers.user import UserSerializer
from ..serializers.todo import TodoSerializer
from ..serializers.post import PostSerializer
from ..serializers.album import AlbumSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # <-- Burası zorunlu
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def todos(self, request, pk=None):
        user = self.get_object()
        todos = user.todos.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        user = self.get_object()
        posts = user.posts.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def albums(self, request, pk=None):
        user = self.get_object()
        albums = user.albums.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)