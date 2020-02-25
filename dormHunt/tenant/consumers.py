from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from tenant.models import Message, MessageRoom
from user.models import User

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        this_room = data['room']
        messages = Message.last_messages(this_room)
        content = {
            'command' : 'messages',
            'messages' : self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data["from"]
        room = data["room"]
        author_user = User.objects.filter(username=author)[0]
        this_room = MessageRoom.objects.filter(name=room)[0]
        message = Message.objects.create(
            room=this_room,
            author=author_user,
            content=data['message'])
        content = {
            'command' : 'new_message',
            'message' : self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def delete_message(self, data):
        message_pk = data['message']
        this_message = Message.objects.get(pk=message_pk)
        this_message.delete()
        # print(data['message'])

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': message.pk,
            'author' : message.author.username,
            'content' : message.content,
            'picture' : message.author.userprofile.picture.url,
            'created_at' : str(message.created_at)
        }


    commands = {
        'fetch_messages' : fetch_messages,
        'new_message' : new_message,
        'remove_message': delete_message,
    }



    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))