from rest_framework import serializers
from models import Message, Conversation
from django.contrib.auth import get_user_model



class Users(serializers.ModelSerializer):
     
    class Meta:
        Users = get_user_model()
        model = Users
        fields = ['__all__']

    

class conversation(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['__all__']

class message(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['__all__']

