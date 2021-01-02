from rest_framework import routers
from django.urls import include, path
from CommunicationService.views import MessageDetail, MessageList

urlpatterns = [
    path('messagedetail/',MessageDetail),
    path('messagelist/',MessageList),
    
]