from rest_framework import routers
from .views import UserList,Login,UserDetail
from django.urls import include, path
urlpatterns = [
    path('userlist/',UserList),
    path('userdetail/',UserDetail),
    path('login/',Login),
]