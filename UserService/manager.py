from .models import User
from django.db import models
from .serializer import UserSerializer
class UserManager():
    def create(self,validated_data):
        insertserializer = UserSerializer()
        insertserializer.create(validated_data)

    def delete(self,pk):
        user = User.objects.get(pk=pk)
        user.if_delete = False
        user.save()
    
    def update(self,pk,validated_data):
        user = User.objects.get(pk=pk)
        updateserializer = UserSerializer()
        user = updateserializer.update(instance=user,validated_data=validated_data)
        user.save()
    
    def all(self):
        return User.objects.all()

    def find(self,query_criteria):
        return User.objects.filter(**query_criteria)
    
    def find_one(self,pk):
        return User.objects.get(pk=pk)