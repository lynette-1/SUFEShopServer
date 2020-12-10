from rest_framework import routers
from .views import UserList,Login,UserDetail
from django.urls import include, path
urlpatterns = [
    path('userlis/',UserList),
    path('userdetail/',UserDetail),
    path('login/',Login),
]