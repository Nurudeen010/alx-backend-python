from rest_framework import viewsets, status, filters
from .serializers import conversation, message
from .models import Conversation, Message
from rest_framework.response import Response


class ConversationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Conversation.objects.all()
        filter_backends = [filters.OrderingFilter]
        ordering_fields = ['created_at']  # Fields for ordering
        serializer = conversation(queryset, many=True)
        response = serializer.data
        return Response(response)
        
        

class MessageViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Message.objects.all()
        filter_backends = [filters.OrderingFilter]
        ordering_fields = ['sent_at']  # Fields for ordering
        serializer = message(queryset, many=True)
        return Response(serializer.data)