from django.db import models

# Create your models here.
#用户
class User(models.Model):
    SEX_CHOICES = (
        ('MALE','男性'),
        ('FEMALE','女性'),
    )
    ACCOUNT_STATE_CHOICES = (
        ('AVAILABLE','可用'),
        ('DISABLE','禁用'),
    )
    ONLINE_STATE_CHOICES = (
        ('ONLINE','在线'),
        ('OFFLINE','离线'),
    )
    user_id = models.AutoField(primary_key=True,unique=True)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    avatar  = models.ImageField()
    real_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    account_state = models.CharField(choices=ACCOUNT_STATE_CHOICES)
    credit_score = models.IntegerField()
    online_state = models.CharField(choices=ONLINE_STATE_CHOICES)
    identity = models.CharField()
    