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
    IDENTITY_CHOICES = (
        ('USER','用户'),
        ('ADMINISTRATOR','管理员'),
    )
    user_id = models.AutoField(primary_key=True,unique=True)
    user_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30,default = 'new_user')
    password = models.CharField(max_length=20)
    avatar  = models.ImageField()
    real_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6,choices=SEX_CHOICES)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    account_state = models.CharField(choices=ACCOUNT_STATE_CHOICES,max_length=20)
    credit_score = models.IntegerField(default=80)
    online_state = models.CharField(choices=ONLINE_STATE_CHOICES,max_length=20)
    identity = models.CharField(choices=IDENTITY_CHOICES,default='USER',max_length=20)
    if_delete = models.BooleanField(default=False)