from UserService.models import User
from UserService.serializer import UserSerializer
from CommodityService.models import Commodity
from CommodityService.serializer import CommoditySerializer
from OrderService.models import Order,BuyerReview,SellerReview,PaymentRecord
from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
    ORDER_STATUS = (
        ("paying", "待付款"),
        ("paid", "已付款"),
        ("refunded", "已退款"),
        ("cancelled", "已取消"),
    )

    commodity = serializers.CharField(label="商品")
    seller = serializers.CharField(label="卖家")
    buyer = serializers.CharField(label="买家")
    amount = serializers.FloatField(label="订单金额")
    order_state = serializers.CharField(choices=ORDER_STATUS, label="订单状态")
    order_time = serializers.DateTimeField(label="下单时间")

    def create(self,validated_data):
        return Order.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return Order.objects.update(pk,validated_data)


class BuyerReviewSerializer(serializers.Serializer):
    order = serializers.CharField(label="订单")
    score = serializers.IntegerField(label="综合评分")
    comment = serializers.CharField(label="文字评价")
    review_time = serializers.DateTimeField(label="评价时间")

    def create(self,validated_data):
        return BuyerReview.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return BuyerReview.objects.update(pk,validated_data)


class SellerReviewSerializer(serializers.Serializer):
    order = serializers.CharField(label="订单")
    commodity_quality = serializers.IntegerField(label="商品质量")
    deal_speed = serializers.IntegerField(label="交易速度")
    seller_attitude = serializers.IntegerField(label="卖家态度")
    comment = serializers.CharField(label="文字评价")
    review_time = serializers.DateTimeField(label="评价时间")

    def create(self,validated_data):
        return SellerReview.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return SellerReview.objects.update(pk,validated_data)


class PaymentRecordSerializer(serializers.Serializer):
    PAYMENT_TYPE = (
        ("B2P", "买家付款给平台"),
        ("P2S", "平台付款给卖家"),
        ("S2B", "卖家退款给买家"),
        ("P2B", "平台退款给买家"),
    )

    PAYMENT_PLATFORM = (
        ("alipay", "支付宝"),
        ("wechat", "微信"),
    )

    order = serializers.CharField(label="订单ID")
    payment_id = serializers.CharField(label="支付记录ID")
    amount = serializers.FloatField(label="支付金额")
    payment_type = serializers.CharField(choices=PAYMENT_TYPE, label="支付类型")
    payment_platform = serializers.CharField(choices=PAYMENT_PLATFORM, label="支付平台")
    payment_time = serializers.DateTimeField(label="支付时间")

    def create(self,validated_data):
        return PaymentRecord.objects.create(**validated_data)

    def update(self,pk,validated_data):
        return PaymentRecord.objects.update(pk,validated_data)