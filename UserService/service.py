from .manager import UserManager

class UserService():
    def insertUserInfo(self,validated_data):
        usermanager=UserManager()
        usermanager.create(validated_data=validated_data)

    def getUserDetail(self,pk):
        usermanager=UserManager()
        usermanager.find_one(pk=pk)
    
    def getUserList(self,query_criteria=None):
        usermanager=UserManager()
        if query_criteria ==None:
            return usermanager.all()
        else: 
            return usermanager.find(query_criteria)
            
    def updateUserDetail(self,pk):
        usermanager=UserManager()
        return usermanager.find_one(pk=pk)