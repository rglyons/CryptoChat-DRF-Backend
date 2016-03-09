from CryptoChat.models import Conversation, Message, PublicKey
from django.contrib.auth.models import User
from rest_framework import serializers

'''
Serializers are what we use to tell Django how to convert an object into JSON.
Hyperlinked models use URLs to determine what object to gather data about. They
also allow object relationships to be represented as hyperlinks to the related
object(s).
'''

# Represent User as JSON
class UserSerializer(serializers.HyperlinkedModelSerializer):

    # relate user to conversations that another user started with him/her
    conversationLeader = serializers.HyperlinkedRelatedField(queryset=Conversation.objects.all(), many=True,
                                                        view_name='conversation-detail')
    # relate user to conversations that he/she started with another user
    conversationFollower = serializers.HyperlinkedRelatedField(queryset=Conversation.objects.all(), many=True,
                                                        view_name='conversation-detail')
    # relate user to his/her public encryption key
    publicKey = serializers.HyperlinkedRelatedField(queryset=PublicKey.objects.all(), many=False, view_name='publickey-detail')

    class Meta:
        model = User
        # use the following fields and their values when representing a User with JSON
        fields = ('url', 'username', 'publicKey', 'conversationLeader', 'conversationFollower')

class PublicKeySerializer(serializers.HyperlinkedModelSerializer):

    # relate a public key to its user
    user = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), many=False, view_name='user-detail')

    class Meta:
        model = PublicKey
        # use the following fields and their values when representing a Public Key with JSON
        fields = ('url', 'key', 'user')


class ConversationSerializer(serializers.HyperlinkedModelSerializer):

    # take participant_1's username and use that for the serialization
    # participant_1 = serializers.ReadOnlyField(source='participant_1.username')

    # relate conversation to all of the messages within it
    messages = serializers.HyperlinkedRelatedField(queryset=Message.objects.all(), many=True, view_name='message-detail')

    class Meta:
        model = Conversation
        # use the following fields and their values when representing a Conversation with JSON
        fields = ('url', 'participant_1', 'participant_2', 'messages')


class MessageSerializer(serializers.HyperlinkedModelSerializer):

    # take sentBy's username and use that for the serialization
    sentBy = serializers.ReadOnlyField(source='sentBy.username')

    class Meta:
        model = Message
        # use the following fields and their values when representing a Message with JSON
        fields = ('url', 'conversation', 'sentTime', 'encrypted', 'sentBy', 'sentTo', 'text')
