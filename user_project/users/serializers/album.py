from rest_framework import serializers
from ..models.album import Album
from ..serializers.photo import PhotoSerializer

class AlbumSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'userId', 'title', 'photos']
        