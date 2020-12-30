from rest_framework import routers
from .views import CommodityDetail,CommodityList,AuditCommodityList,BrowseHistoryList
from django.urls import include, path
urlpatterns = [
    path('commoditydetail/',CommodityDetail),
    path('commoditylist/',CommodityList),
    path('auditcommoditylist/',AuditCommodityList),
    path('browsehistorylist/',BrowseHistoryList),
    
]