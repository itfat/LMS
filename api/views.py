from django.shortcuts import render
from user.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

# class UsersView(APIView):
#     def get(self, request):
#         queryset = User.objects.all().order_by("name")
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
    

# class UserView(APIView):
#     def single_user(self, id_arg):
#         try:
#             queryset = User.objects.get(id=id_arg)
#             return queryset
#         except User.DoesNotExist:
#             return None
#     def get(self, request, id_arg):
#         queryset = self.single_user(id_arg)
#         if queryset:

#             serializer = UserSerializer(queryset)
#             return Response(serializer.data)
#         else:
#             return Response({"message": f"The user with id {id_arg} does not exist"}, status.HTTP_400_BAD_REQUEST)
        



    

