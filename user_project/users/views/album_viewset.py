from rest_framework import viewsets
from ..models.album import Album
from ..serializers.album import AlbumSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
