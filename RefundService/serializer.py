from rest_framework import serializers
from .models import RefundApplication

class RefundApplicationSerializer(serializers.Serializer):
    REFUND_STATE_CHOICES =(
        ('TO_BE_REVIEWED','待审核'),
        ('APPROVED','同意退款'),
        ('REJECTED','拒绝退款'),
    )
    refund_state = serializers.ChoiceField(choices=REFUND_STATE_CHOICES,label='退款状态')
    refund_reason = serializers.CharField(label='退款理由')
    refund_time = serializers.DateTimeField(label='退款时间')
    order = serializers.CharField(label='订单编号')
    if_delete = serializers.BooleanField(label='是否删除')
    def create(self,validated_data):
        return RefundApplication.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.refund_state = validated_data.get('refund_state',instance.refund_state)
        instance.refund_reason = validated_data.get('refund_reason',instance.refund_reason)
        instance.refund_time = validated_data.get('refund_time',instance.refund_time)
        instance.order = validated_data.get('order',instance.order)
        instance.if_delete = validated_data.get('if_delete',instance.if_delete)
        instance.save()
        return instance
# refund_id = models.AutoField(primary_key=True)
#     refund_state = models.CharField(choices=REFUND_STATE_CHOICES)
#     refund_apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
#     refund_reason = models.CharField(max_length=20)
#     refund_time = models.DateTimeField(auto_now=False, auto_now_add=False)
#     '''！！！外键引用有可能出现问题！！！'''
#     order = models.ForeignKey("OrderService.Order",to_field='order_id',on_delete=models.CASCADE)