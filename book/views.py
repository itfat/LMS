from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from book.models import Book

@csrf_exempt
def book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        queryset = Book.objects.all().order_by("name")
        serializer = BookSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        


def single_book(id_arg):
    try:
        queryset = Book.objects.get(id=id_arg)
        return queryset
    except Book.DoesNotExist:
        return None
    
@csrf_exempt
def book_detail(request, id_arg):
    """
    Retrieve, update or delete a user.
    """
    queryset = single_book(id_arg)

    if request.method == 'GET':
        if queryset:
            serializer = BookSerializer(queryset)
            return JsonResponse(serializer.data)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'PUT':   
        if queryset:
            data = JSONParser().parse(request)
            serializer = BookSerializer(data=data)
            if serializer.is_valid():       
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        if queryset:
            queryset.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)





