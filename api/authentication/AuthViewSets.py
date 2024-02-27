
from django.http import JsonResponse
from rest_framework import viewsets,generics
from rest_framework_simplejwt.views import TokenObtainPairView                           
from .AuthSerializers import UserSerialiser, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken ,AccessToken               
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

from .models import Users


class  createUser(APIView):

    def post(self,request):
       serializer=UserSerialiser(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)



    queryset = Users.objects.all()
    serializer_class = UserSerialiser
    permission_classes=[AllowAny]
    

class login(APIView):
    serializer_class=UserLoginSerializer
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh=RefreshToken.for_user(user)
            access=AccessToken.for_user(user)
            return JsonResponse({"refresh":str(refresh),
                                 "access":str(access),
                                 })
        else:
            return JsonResponse({"error":"invalid username or password"})
        
        
    
       
   



