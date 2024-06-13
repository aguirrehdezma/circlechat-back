import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from chat_messages.models import Message
from chatrooms.models import Chatroom

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            content = text_data_json['content']
            chatroom = text_data_json['chatroom']
            user_id = text_data_json['user_id']

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'content': content,
                    'chatroom': chatroom,
                    'user_id': user_id,
                }
            )

            await self.save_message(chatroom, content)
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({'error': 'Invalid JSON'}))
        except KeyError:
            await self.send(text_data=json.dumps({'error': 'Missing required data'}))

    async def chat_message(self, event):
        content = event['content']
        chatroom = event['chatroom']
        user_id = event['user_id']

        await self.send(text=json.dumps({
            'content': content,
            'chatroom': chatroom,
            'user_id': user_id,
        }))

    @sync_to_async
    def save_message(self, chatroom_id, content):
        chatroom = Chatroom.objects.get(pk=chatroom_id)
        user = self.scope['user']
        Message.objects.create(chatroom_id=chatroom_id, content=content, created_by=user)
