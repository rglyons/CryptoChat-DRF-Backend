from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from CryptoChat.models import Conversation, Message, PublicKey
from django.contrib.auth.models import User
from CryptoChat.serializers import UserSerializer, ConversationSerializer, MessageSerializer, PublicKeySerializer

# Viewsets for each model - allows for data retrieval and updating
# HTTP Request functionality is built in to viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PublicKeyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows public keys to be viewed or edited.
    """
    queryset = PublicKey.objects.all()
    serializer_class = PublicKeySerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conversations to be viewed or edited.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    # when we create a conversation, initialize the participant_1
    # field to the username of the user who makes the request
    def perform_create(self, serializer):
        serializer.save(participant_1=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # when we create a message, initialize the sentBy
    # field to the username of the user who makes the request
    def perform_create(self, serializer):
        serializer.save(sentBy=self.request.user)