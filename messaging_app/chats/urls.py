from django.urls import path, include
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet
from rest_framework_nested.routers import NestedDefaultRouter

router = routers.DefaultRouter()
router.register(r'conversation', ConversationViewSet, basename='conversation')


#Nested router for messages under conversation
conversation_router = NestedDefaultRouter(router, r'conversation', lookup='conversation')
conversation_router.register(r'message', MessageViewSet, basename='conversation-message')

urlpatterns = [
    path('', include(router.urls)),
     path('', include(conversation_router.urls)),
]