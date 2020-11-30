from rest_framework import serializers
from .models import RefunApplication

class RefunApplicationSerializer(serializers.Serializer):
    refund_id = serializers.CharField(read_only=True)
    refund_state = serializers.CharField()
    refund_apply_time = serializers.DateTimeField()
    refund_reason = serializers.CharField()
    refund_time = serializers.DateTimeField()
    order = serializers.CharField()

    def create(self,validated_data):
        return RefunApplication.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.refund_state = validated_data.get('refund_state',instance.refund_state)
        instance.refund_apply_time = validated_data.get('refund_apply_time',instance.refund_apply_time)
        instance.refund_reason = validated_data.get('refund_reason',instance.refund_reason)
        instance.refund_time = validated_data.get('refund_time',instance.refund_time)
        instance.order = validated_data.get('order',instance.order)
# refund_id = models.AutoField(primary_key=True)
#     refund_state = models.CharField(choices=REFUND_STATE_CHOICES)
#     refund_apply_time = models.DateTimeField(auto_now=False, auto_now_add=True)
#     refund_reason = models.CharField(max_length=20)
#     refund_time = models.DateTimeField(auto_now=False, auto_now_add=False)
#     '''！！！外键引用有可能出现问题！！！'''
#     order = models.ForeignKey("OrderService.Order",to_field='order_id',on_delete=models.CASCADE)