from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate
class UserView(APIView):

    def post(self,request):
        
        data=request.data
        newUser=User(username=data['username'],is_superuser=data['is_superuser'])
        newUser.set_password(data['password'])

        newUser.save()

        return Response("user created")
    
class UserLoginView(APIView):

    def post(self,request):

        data=request.data
        user_verification=authenticate(username=data['username'],password=data['password'])
       
        if user_verification ==None:

            return Response("Incorrect credentials Try again...!!!!")
        return Response("Login successfull")
