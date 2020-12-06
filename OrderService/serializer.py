from UserService.models import User
from UserService.serializer import UserSerializer
from CommodityService.models import Commodity
from CommodityService.serializer import CommoditySerializer
from OrderService.models import Order,BuyerReview,SellerReview,PaymentRecord
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class BuyerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerReview
        fields = "__all__"

class SellerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerReview
        fields = "__all__"

class PaymentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRecord
        fields = "__all__"