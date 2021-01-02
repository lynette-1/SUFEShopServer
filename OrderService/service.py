from UserService.models import User
from CommodityService.models import Commodity
from OrderService.models import Order,BuyerReview,SellerReview,PaymentRecord

class OrderService():
    @staticmethod
    def listBoughtOrder(buyer):
        return Order.objects.filter(buyer=buyer)

    @staticmethod
    def listSoldOrder(seller):
        return Order.objects.filter(seller=seller)

    @staticmethod
    def getOrderDetail(order_id):
        return Order.objects.get(pk=order_id)

    @staticmethod
    def insertOrder(validated_data):
        orderdata = validated_data['commodity','seller','buyer','amount']
        Order.objects.create(orderdata)

    @staticmethod
    def payOrder(order_id,validated_data):
        OrderService.pay(order_id)
        Order.objects.update(order_id,{'order_state':"已付款"})
        OrderService.insertPaymentRecord(validated_data)

    @staticmethod
    def insertPaymentRecord(validated_data):
        paymentRecorddata = validated_data['order','amount','payment_type','payment_platform']
        PaymentRecord.objects.create(paymentRecorddata)
        
    @staticmethod
    def pay(order_id):
        pass
    
    @staticmethod
    def insertSellerReview(validated_data):
        sellerreviewdata = validated_data['order','commodity_quality','deal_speed','seller_attitude','comment']
        SellerReview.objects.create(sellerreviewdata)

    @staticmethod
    def insertBuyerReview(validated_data):
        buyerreviewdata = validated_data['order','score','comment']
        BuyerReview.objects.create(buyerreviewdata)
