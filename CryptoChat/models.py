from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

import json

#User Model extension
class MyUser(models.Model) :
    user = models.OneToOneField(User)
    public_key = models.IntegerField(default=1)

#Conversation Model
class Conversation (models.Model) :
    participant_1 = models.ForeignKey('auth.User', related_name='conversationLeader')
    participant_2 = models.ForeignKey('auth.User', related_name='conversationFollower')

    #in order to access message history we must store a list of messages in
    #the "messagses" field. To do this we will convert the message list to
    #a string to store it, and back to a list when we access it

    #convert to string to store
    def setMessages (self, msg) :
        self.messages = json.dumps(msg)

    #convert to list to access
    def getMessages (self) :
        return json.loads(self.messages)

#Message Model
class Message (models.Model) :
    text = models.CharField(max_length=2000, blank=True, default='')
    sentTime = models.DateTimeField(auto_now_add=True)
    encrypted = models.BooleanField(default=False)
    conversation = models.ForeignKey(Conversation, related_name='messages', default='')
    sentBy = models.ForeignKey('auth.User', related_name='messages')
    sentTo = models.ForeignKey('auth.User', default='')

    def send (self, msg) :
        self.conversation.getMessages().append(msg)

