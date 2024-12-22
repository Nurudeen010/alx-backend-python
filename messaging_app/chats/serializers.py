from rest_framework import serializers
from .models import Message, Conversation
from django.contrib.auth import get_user_model

Users = get_user_model()

class User(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirmed_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Users
        fields = ['email', 'first_name', 'last_name', 
                  'phone_number', 'role', 'password', 'confirmed_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirmed_password']:
            raise serializers.ValidationError({"password": "The passwords do not match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirmed_password')
        user = Users.objects.create_user(**validated_data)
        return user

class message(serializers.Serializer):
    message_id = serializers.UUIDField(required=True)
    sender_id = serializers.IntegerField(required=True)
    message_body = serializers.CharField(required=True)
    sent_at = serializers.TimeField(required=True)

    def validate_message_body(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('The message_body must not be empty')
        return value

class conversation(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participant_id', 'created_at', 'messages']

    def get_messages(self, obj):
        # Assuming Conversation has a related_name='messages' on Message
        return message(obj.messages.all(), many=True).data