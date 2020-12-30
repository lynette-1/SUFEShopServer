from rest_framework import routers
from .views import RefundDetail
from django.urls import include, path
urlpatterns = [
    path('refunddetail/',RefundDetail),
]