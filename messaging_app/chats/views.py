from rest_framework import viewsets, status, filters, generics
from .serializers import conversation, message, User
from .models import Conversation, Message, AbstractBaseUser
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegisterationView(generics.CreateAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = User


class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


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