from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .service import UserService
# Create your views here.
# class UserViewSet (ModelViewSet):
class UserList(APIView):
    #根据查询条件获取数据，没有返回查询条件就获取全部数据
    def get(self,request,query_criteria=None):
        userservice = UserService()
        query_set = userservice.getUserList(query_criteria=query_criteria)
        serializer = UserSerializer(query_set,many=True)
        return Response(serializer.data)    

class UserDetail(APIView):
    def get(self,request,pk):
        userservice = UserService()
        user = userservice.getUserDetail(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)  

    def delete(self,request,pk):
        userservice = UserService()
        userservice.updateUserDetail