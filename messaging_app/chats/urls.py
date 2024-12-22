from django.urls import path, include
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet, UserLoginView, UserRegisterationView
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'conversation', ConversationViewSet, basename='conversation')
router.register(r'message', MessageViewSet, basename='message')

#Nested router for messages under conversation
conversation_router = NestedDefaultRouter(router, r'conversation', lookup='conversation')
conversation_router.register(r'message', MessageViewSet, basename='conversation-message')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversation_router.urls)),
    path('register/', UserRegisterationView.as_view()),
    path('login/', UserLoginView.as_view())

]