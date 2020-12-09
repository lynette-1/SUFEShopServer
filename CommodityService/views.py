from django.shortcuts import render
from .service import CommodityService
from rest_framework.views import APIView
from rest_framework.response import Response


class CommodityDetail(APIView):

    def get(self, request, commodity_id):
        serializer = CommodityService.getCommodityDetail(commodity_id=commodity_id)
        return Response(serializer.data)
