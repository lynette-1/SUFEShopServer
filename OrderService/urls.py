from rest_framework import routers
from django.urls import include, path
from OrderService.views import OrderDetail,BoughtOrderList,SoldOrderList,BuyerReviewDetail,SellerReviewDetail,PayOrderDetail,GenerateOrderDetail

urlpatterns = [
    path('orderdetail/',OrderDetail.as_view()),
    path('boughtorderlist/',BoughtOrderList.as_view()),
    path('soldorderlist/',SoldOrderList.as_view()),
    path('buyerreviewdetail/',BuyerReviewDetail.as_view()),
    path('sellerreviewdetail/',SellerReviewDetail.as_view()),
    path('payorderdetail/',PayOrderDetail.as_view()),
    path('generateorderdetail/',GenerateOrderDetail.as_view()),
    
]