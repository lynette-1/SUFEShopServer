from django.shortcuts import render
from .service import CommodityService
from .serializer import CommoditySerializer,CommodityApplicationSerializer,BrowserHisorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .service import CommodityService

# CommodityItem?
class CommodityDetail(APIView):

    def get(self, request, commodity_id):
        instance = CommodityService.getCommodityDetail(commodity_id=commodity_id)
        serializer = CommoditySerializer(instance)
        return Response(serializer.data)
    def post(self, request):
        serializer=CommoditySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CommodityService.insertCommodity(validated_data=serializer.data)
        return Response(serializer.data)
    def put(self, request, commodity_id):
        serializer=CommoditySerializer(data=request.data)
        CommodityService.updateMyCommodityDetail(commodity_id,serializer.data)
        return Response(serializer.data)
    def delete(self, request, commodity_id):
        return CommodityService.deleteCommodity(commodity_id)

class CommodityList(APIView):
    def get(self, request,user):
        query_set = CommodityService.listMyCommodity(user)
        seriliazer = CommoditySerializer(query_set)
        return Response(seriliazer.data)
    # listcommodities()

class AuditCommodityList(APIView):
    def get(self, request):
        query_set = CommodityService.listUnauditedCommodities()
        seriliazer = CommodityApplicationSerializer(query_set,many=True)
        return Response(seriliazer.data)
    def patch(self, request,application_id):
        serializer = CommodityApplicationSerializer(request.data)
        CommodityService.processUnauditedCommodity(application_id,serializer.data)
        return Response(serializer.data)
class BrowseHistoryList(APIView):
    def get(self, request,user):
        query_set = CommodityService.listBrowseHistory(user)
        serializer = BrowserHisorySerializer(query_set,many=True)
        return Response(serializer.data)