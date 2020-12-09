from django.db import models

# 商品管理器
class CommodityManager(models.Manager):
    pass

#商品
class Commodity(models.Model):
    commodity_id = models.AutoField(primary_key=True)
    commodity_name = models.CharField(max_length=50)
    commodity_type = models.CharField( max_length=20)
    commodity_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    detail = models.TextField()
    on_shelf_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    if_delete = models.BooleanField(default=False)
    
    objects = CommodityManager()

#申请记录
class CommodityApplication(models.Model):
    APPLICATION_STATE_CHOICES = (
        ('TO_BE_REVIEWED','待审核'),
        ('APPROVED','审核通过'),
        ('REJECTED','审核未通过'),
    )
    application_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("UserService.User",related_name='applier',to_field='user_id',on_delete=models.CASCADE)
    Commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
    apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    application_state = models.CharField(choices=APPLICATION_STATE_CHOICES,max_length=20)
    auditor = models.ForeignKey("UserService.User",related_name='auditor',to_field='user_id',on_delete=models.CASCADE,blank=True)
    audit_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    if_delete = models.BooleanField(default=False)

#浏览记录
class BrowserHisory(models.Model):
    browser_history_id = models.AutoField(primary_key=True)
    commodity = models.ForeignKey("Commodity",to_field='commodity_id',on_delete=models.CASCADE)
    user = models.ForeignKey("UserService.User",to_field='user_id', on_delete=models.CASCADE)
    browse_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    if_delete = models.BooleanField(default=False)

