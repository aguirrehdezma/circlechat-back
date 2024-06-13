from django.urls import path
from . import views

urlpatterns = [
    path('get_messages/<uuid:chatroom_id>/', views.get_messages, name="get_messages"),
]
