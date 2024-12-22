from rest_framework import serializers
from .models import Message, Conversation
from django.contrib.auth import get_user_model



class Users(serializers.ModelSerializer):
     
    class Meta:
        Users = get_user_model()
        model = Users
        fields = ['__all__']

class message(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'message_body', 'sent_at']


class conversation(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participant_id', 'created_at', 'messages']

    def get_messages(self, obj):
        return obj.message.message_body


