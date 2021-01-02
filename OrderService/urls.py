from rest_framework import routers
from django.urls import include, path
from OrderService.views import OrderDetail,BoughtOrderList,SoldOrderList,BuyerReviewDetail,SellerReviewDetail,PayOrderDetail,GenerateOrderDetail

urlpatterns = [
    path('orderdetail/',OrderDetail),
    path('boughtorderlist/',BoughtOrderList),
    path('soldorderlist/',SoldOrderList),
    path('buyerreviewdetail/',BuyerReviewDetail),
    path('sellerreviewdetail/',SellerReviewDetail),
    path('payorderdetail/',PayOrderDetail),
    path('generateorderdetail/',GenerateOrderDetail),
    
]