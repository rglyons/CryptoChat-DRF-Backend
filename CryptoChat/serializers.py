from CryptoChat.models import Conversation, Message
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    conversationLeader = serializers.HyperlinkedRelatedField(queryset=Conversation.objects.all(), many=True,
                                                        view_name='conversation-detail')
    conversationFollower = serializers.HyperlinkedRelatedField(queryset=Conversation.objects.all(), many=True,
                                                        view_name='conversation-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'conversationLeader', 'conversationFollower')


class ConversationSerializer(serializers.HyperlinkedModelSerializer):

    participant_1 = serializers.ReadOnlyField(source='participant_1.username')

    messages = serializers.HyperlinkedRelatedField(queryset=Message.objects.all(), many=True, view_name='message-detail')

    class Meta:
        model = Conversation
        fields = ('url', 'participant_1', 'participant_2', 'messages')


class MessageSerializer(serializers.HyperlinkedModelSerializer):

    sentBy = serializers.ReadOnlyField(source='sentBy.username')

    class Meta:
        model = Message
        fields = ('url', 'conversation', 'sentTime', 'encrypted', 'sentBy', 'sentTo', 'text')
