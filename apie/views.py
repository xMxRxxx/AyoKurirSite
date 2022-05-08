from django.shortcuts import render

# Create your views here.
from ak_company import models 
from .serializer import *
from rest_framework import generics

class listTodoItem(generics.ListCreateAPIView):
    queryset = models.Item.objects.all()
    serializer_class = itemSerializer


class detailTodoItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Item.objects.all()
    serializer_class = itemSerializer

class listTodoUser(generics.ListCreateAPIView):
    queryset = models.userProfil.objects.all()
    serializer_class = userSerializer

class listTodoMessage(generics.ListCreateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = messageSerializer

