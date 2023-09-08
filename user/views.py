
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from user.serializers import UserSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from user.models import User
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        queryset = User.objects.all().order_by("name")
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def single_user(id_arg):
    try:
        queryset = User.objects.get(id=id_arg)
        return queryset
    except User.DoesNotExist:
        return None
    
@csrf_exempt
def user_detail(request, id_arg):
    """
    Retrieve, update or delete a user.
    """
    queryset = single_user(id_arg)

    if request.method == 'GET':
        if queryset:
            serializer = UserSerializer(queryset)
            return JsonResponse(serializer.data)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'PUT':
        if queryset:
            data = JSONParser().parse(request)
            serializer = UserSerializer(queryset, data=data)
            if serializer.is_valid():       
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        if queryset:
            queryset.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)






