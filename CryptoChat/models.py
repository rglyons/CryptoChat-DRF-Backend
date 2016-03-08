from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

import json

# This project uses the default, built-in Django User model
# Models define the attributes of an object that are important to
# keep record of

#Public Key Model
class PublicKey (models.Model) :
    user = models.OneToOneField('auth.User', related_name='publicKey')
    key = models.CharField(max_length=1000, default='')

#Conversation Model
class Conversation (models.Model) :
    participant_1 = models.ForeignKey('auth.User', related_name='conversationLeader')
    participant_2 = models.ForeignKey('auth.User', related_name='conversationFollower')

#Message Model
class Message (models.Model) :
    text = models.CharField(max_length=2000, blank=True, default='')
    sentTime = models.DateTimeField(auto_now_add=True)
    encrypted = models.BooleanField(default=False)
    conversation = models.ForeignKey(Conversation, related_name='messages', default='')
    sentBy = models.ForeignKey('auth.User', related_name='messages')
    sentTo = models.ForeignKey('auth.User', default='')

