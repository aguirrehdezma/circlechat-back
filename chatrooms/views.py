from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Chatroom
from .serializers import ChatroomSerializer

@api_view(['GET']) # Retrieve the chatrooms to show in the lobby
def get_chatrooms(request):
    chatrooms = Chatroom.objects.all()
    serializer = ChatroomSerializer(chatrooms, many=True)
    return Response(serializer.data)

@api_view(['POST']) # Create the chatroom in the DB
def create_chatroom(request):
    name = request.data.get('name')
    chatroom = Chatroom.objects.create(name=name)
    chatroom.save()
    return Response({'messages': 'created'})

@api_view(['POST']) # Retrieve chatroom info for its own page
def get_chatroom(request, chatroom_id):
    chatroom = Chatroom.objects.get(pk=chatroom_id)
    serializer = ChatroomSerializer(chatroom)
    return Response(serializer.data)
