from rest_framework import routers
from .views import CommodityDetail,CommodityList,AuditCommodityList,BrowseHistoryList
from django.urls import include, path
urlpatterns = [
    path('commoditydetail/',CommodityDetail.as_view()),
    path('commoditylist/',CommodityList.as_view()),
    path('auditcommoditylist/',AuditCommodityList.as_view()),
    path('browsehistorylist/',BrowseHistoryList.as_view()),
]