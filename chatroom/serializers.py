from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from chatroom.models import MessageModel
from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers


class MessageModelSerializer(ModelSerializer):
    user = CharField(source='user.username', read_only=True)
    recipient = CharField(source='recipient.username')

    def create(self, validated_data):
        user = self.context['request'].user
        recipient = get_object_or_404(
            User, username=validated_data['recipient']['username'])
        msg = MessageModel(recipient=recipient,
                           body=validated_data['body'],
                           user=user)
        msg.save()
        return msg

    class Meta:
        model = MessageModel
        fields = ('id', 'user', 'recipient', 'timestamp', 'body')


class UserModelSerializer(ModelSerializer):
    active = serializers.CharField(source='user_status.active')
    class Meta:
        model = User
        fields = ('username','active')
