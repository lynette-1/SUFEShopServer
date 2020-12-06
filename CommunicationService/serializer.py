from UserService.models import User
from UserService.serializer import UserSerializer
from CommunicationService.models import Message
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"