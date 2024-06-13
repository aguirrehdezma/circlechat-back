from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

@api_view(['GET']) # Sign in purposes
def get_user_info(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
