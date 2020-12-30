from .serializer import RefundApplicationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .service import RefundApplicationService
# Create your views here.

def RefundDetail(APIView):
    def get(self,request,pk):
        refundapplication = RefundApplicationService.getRefundDetail(pk=pk)
        serializer = RefundApplicationSerializer(refundapplication)
        return Response(serializer.data)
    
    def patch(self,request,pk):
        serializer=RefundApplicationSerializer(data=request.data)
        RefundApplicationService.processRefund(pk,serializer.data)
        return Response(serializer.data)
