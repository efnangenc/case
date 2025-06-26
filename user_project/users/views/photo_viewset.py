from rest_framework import viewsets
from ..models.photo import Photo
from ..serializers.photo import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
