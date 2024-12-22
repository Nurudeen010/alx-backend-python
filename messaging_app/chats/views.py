from rest_framework import viewsets, status
from .serializers import conversation, message
from .models import Conversation, Message
from rest_framework.response import Response


class ConversationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Conversation.objects.all()
        serializer = conversation(queryset, many=True)
        response = serializer.data
        return Response(response)
        
        

class MessageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Message.objects.all()
        serializer = message(queryset, many=True)
        return Response(serializer.data)