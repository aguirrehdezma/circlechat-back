from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MessageSerializer
from chatrooms.models import Chatroom

@api_view(['POST'])
def get_messages(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    messages = chatroom.messages.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
