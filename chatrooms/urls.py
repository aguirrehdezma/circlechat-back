from django.urls import path
from . import views

urlpatterns = [
    path('get_chatrooms/', views.get_chatrooms, name="get_chatrooms"),
    path('create_chatroom/', views.create_chatroom, name="create_chatroom"),
    path('get_chatroom/<uuid:chatroom_id>/', views.get_chatroom, name="get_chatroom"),
]
