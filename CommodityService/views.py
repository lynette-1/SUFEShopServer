from django.shortcuts import render
from .service import CommodityService
from .serializer import CommodityDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CommodityDetail(APIView):

    def get(self, request, commodity_id):
        instance = CommodityService.getCommodityDetail(commodity_id=commodity_id)
        serializer = CommodityDetailSerializer(instance)
        return Response(serializer.data)
