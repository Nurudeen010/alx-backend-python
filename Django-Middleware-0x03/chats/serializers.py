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

class message(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['message_id','sender_id', 'sent_at', 'conversation']
    
    def create(self, validated_data):
        # Automatically set sender_id to the logged-in user
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['sender_id'] = request.user
        return super().create(validated_data)

class conversation(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants_id', 'created_at', 'messages']
        read_only_fields = ['conversation_id', 'participants_id', 'created_at']

    def create(self, validated_data):
        # Automatically set sender_id to the logged-in user
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['participants_id'] = request.user
        return super().create(validated_data)


    def get_messages(self, obj):
        # Assuming Conversation has a related_name='messages' on Message
        messages = obj.messages.all()
        return message(messages, many=True).data