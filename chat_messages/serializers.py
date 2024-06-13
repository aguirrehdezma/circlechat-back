from rest_framework import serializers
from .models import Message
from users.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = (
            'chatroom',
            'content',
            'created_at',
            'created_by',
        )
