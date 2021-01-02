from django.db import models
from datetime import datetime
from UserService.models import User

# Create your models here.
class MessageManager(models.Manager):
    
    def create(self,validated_data):
        return super().create(**validated_data)
    
    def delete(self,pk):
        instance = super().get(pk=pk)
        instance.if_delete = True
        instance.save()
        return instance


class Message(models.Model):
    
    MESSAGE_STATUS = (
        ("read", "已读"),
        ("unread", "未读"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender', verbose_name="源用户")
    receive_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciever',verbose_name="目标用户")
    message_id = models.AutoField(primary_key=True)
    message_content = models.TextField(default="", max_length=200, verbose_name="消息内容")
    message_state = models.CharField(choices=MESSAGE_STATUS, default="未读", max_length=20, verbose_name="消息状态")
    send_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True, verbose_name="发送时间")
    if_delete = models.BooleanField(default=False)
    objects = MessageManager()

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.message_content)