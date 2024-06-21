import uuid
from django.db import models

class Chatroom(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
