from django.forms import ModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    
    queryset = Book.objects.all()
    serializer = BookSerializer

    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

