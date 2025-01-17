from UserService.models import User
from UserService.serializer import UserSerializer
from CommunicationService.models import Message
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    MESSAGE_STATUS = (
        ("read", "已读"),
        ("unread", "未读"),
    )
    
    message_content = serializers.CharField(label="消息内容")
    message_state = serializers.CharField(label="消息状态",choices=MESSAGE_STATUS)
    send_time = serializers.DateTimeField(label="发送时间")

    def create(self,validated_data):
        return Message.objects.create(**validated_data)

