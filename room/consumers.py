import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    online_users = set()  # Множество для хранения онлайн-пользователей

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Добавляем пользователя в онлайн-список
        self.username = self.scope['user'].username
        ChatConsumer.online_users.add(self.username)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Отправляем обновленный список онлайн-пользователей
        await self.send_online_users_count()

    async def disconnect(self, close_code):
        # Удаляем пользователя из онлайн-списка
        ChatConsumer.online_users.remove(self.username)

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Отправляем обновленный список онлайн-пользователей
        await self.send_online_users_count()

    async def send_online_users_count(self):
        online_count = len(ChatConsumer.online_users)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'online_users_count',
                'count': online_count,
                'users': list(ChatConsumer.online_users)
            }
        )

    async def online_users_count(self, event):
        count = event['count']
        users = event['users']

        # Отправляем количество онлайн-пользователей и их имена
        await self.send(text_data=json.dumps({
            'online_count': count,
            'online_users': users
        }))

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message'].strip()

        if not message:
            return

        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room_instance = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room_instance, content=message)
