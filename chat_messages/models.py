from django.contrib.auth.models import User
from django.db import models
from chatrooms.models import Chatroom

class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',) # Show the messages from older to newer
