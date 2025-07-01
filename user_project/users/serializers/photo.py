from rest_framework import serializers
from ..models.photo import Photo

class PhotoSerializer(serializers.ModelSerializer):
    albumId = serializers.PrimaryKeyRelatedField(source='album', read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'albumId', 'title', 'url', 'thumbnailUrl']