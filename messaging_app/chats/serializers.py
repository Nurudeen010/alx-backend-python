from rest_framework import serializers
from .models import Message, Conversation
from django.contrib.auth import get_user_model



class Users(serializers.ModelSerializer):
     
    class Meta:
        Users = get_user_model()
        model = Users
        fields = ['__all__']

class message(serializers.Serializer):
    message_id = serializers.UUIDField()
    sender_id = serializers.IntegerField()
    message_body = serializers.CharField()
    sent_at = serializers.TimeField()

    def validate(self, attrs):
        if attrs['message_body'] == '':
            raise serializers.ValidationError('The message_body must not be empty')
        return attrs
    
class conversation(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participant_id', 'created_at', 'messages']

    def get_messages(self, obj):
        return obj.message.message_body


