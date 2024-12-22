from rest_framework.viewsets import ModelViewSet
from .serializers import conversation, message
from .models import Conversation, Message


class ConversationViewSet(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = conversation

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = message