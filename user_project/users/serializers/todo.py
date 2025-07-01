from rest_framework import serializers
from ..models.todo import Todo

class TodoSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'userId', 'title', 'completed']