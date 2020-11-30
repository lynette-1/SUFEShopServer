from django.db import models

# Create your models here.
#退款记录
class RefundApplication(models.Model):
    REFUND_STATE_CHOICES =(
        ('TO_BE_REVIEWED','待审核'),
        ('APPROVED','同意退款'),
        ('REJECTED','拒绝退款'),
    )
    refund_id = models.AutoField(primary_key=True)
    refund_state = models.CharField(choices=REFUND_STATE_CHOICES,default='TO_BE_REVIEWED')
    refund_apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    refund_reason = models.TextField()
    refund_time = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True)
    '''！！！外键引用有可能出现问题！！！'''
    order = models.ForeignKey("OrderService.Order",to_field='order_id',on_delete=models.CASCADE)
    if_delete = models.BooleanField(default=False)