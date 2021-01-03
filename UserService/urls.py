from rest_framework import routers
from .views import UserList,Login,UserDetail
from django.urls import include, path
urlpatterns = [
    path('userlist/',UserList.as_view()),
    path('userdetail/',UserDetail.as_view()),
    path('login/',Login.as_view()),
]