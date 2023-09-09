
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer = UserSerializer

    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


