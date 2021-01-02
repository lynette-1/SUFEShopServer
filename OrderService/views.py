from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from OrderService.service import OrderService
from OrderService.serializer import OrderSerializer,BuyerReviewSerializer,SellerReviewSerializer,PaymentRecordSerializer

# Create your views here.
class OrderDetail(APIView):
    def get(self, request, order_id):
        instance = OrderService.getOrderDetail(order_id=order_id)
        serializer = OrderSerializer(instance)
        return Response(serializer.data)


class BoughtOrderList(APIView):
    def get(self, request, buyer):
        instance = OrderService.listBoughtOrder(buyer=buyer)
        serializer = OrderSerializer(instance)
        return Response(serializer.data)


class SoldOrderList(APIView):
    def get(self, request, seller):
        instance = OrderService.listSoldOrder(seller=seller)
        serializer = OrderSerializer(instance)
        return Response(serializer.data)


class BuyerReviewDetail(APIView):
    def post(self, request):
        serializer = BuyerReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertBuyerReview(validated_data=serializer.data)
        return Response(serializer.data)


class SellerReviewDetail(APIView):
    def post(self, request):
        serializer = SellerReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertSellerReview(validated_data=serializer.data)
        return Response(serializer.data)
    

class PayOrderDetail(APIView):
    def post(self, request):
        serializer = PaymentRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertPaymentRecord(validated_data=serializer.data)
        return Response(serializer.data)


class GenerateOrderDetail(APIView):
    def post(self, request):
        serializer=OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        OrderService.insertOrder(validated_data=serializer.data)
        return Response(serializer.data)
    

