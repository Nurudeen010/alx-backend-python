from rest_framework import viewsets, status, filters, generics
from .serializers import conversation, message, User
from .models import Conversation, Message, user
from .filters import MessageFilter
from .permissions import IsParticipantOfConversation
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import django_filters


class UserRegisterationView(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = User


class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class ConversationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    def list(self, request):
        queryset = Conversation.objects.all()
        if not queryset.exists():
            return Response({'message': 'No conversations found.'}, status=404)
        serializer = conversation(queryset, many=True)
        response = serializer.data
        return Response(response)
        
    def create(self, request):
        serializer = conversation(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def list(self, request):
        queryset = Message.objects.all()
        filter_backends = (filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
        filterset_class = MessageFilter
        ordering_fields = ['sent_at'] 
        serializer = message(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = message(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)