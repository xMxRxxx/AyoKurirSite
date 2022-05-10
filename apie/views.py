from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.exceptions import BadRequest

# Create your views here.
from ak_company import models 
from .serializer import *
from rest_framework import generics
from django.db.models import Q


class kurirAPI:
    def __init__(self, *args, **kwargs):
        super(CLASS_NAME, self).__init__(*args, **kwargs)



class listTodoItem(generics.ListCreateAPIView):
    queryset = models.Item.objects.all()
    serializer_class = itemSerializer


class detailTodoItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Item.objects.all()
    serializer_class = itemSerializer

class listTodoDetailUser(generics.ListCreateAPIView):
    queryset = models.userProfil.objects.all()
    serializer_class = userSerializer

# class listTodoMessage(generics.ListCreateAPIView):
#     queryset = models.Message.objects.all()
#     serializer_class = messageSerializer

class listTodoImageItem(generics.ListCreateAPIView):
    queryset = models.imageProduct.objects.all()
    serializer_class = imageProductSerializer

@csrf_exempt
def getUser(request, Email=None, Password=None):
    if request.method=="GET":
        try:
            user=models.userProfil.objects.get(Email=email, password=Password)
        except models.userProfil.DoesNotExist:
            raise BadRequest("Invalid...")

        data = userSerializer(user).data

        return JsonResponse(data, safe=False)

    else:
        return JsonResponse('Failed to get user data...', safe=False)

def getListMessages(request, sender=None, receiver=None):
    if request.method=="GET":
        try:
            # user=models.Message.objects.get(Sender=sender, Receiver=receiver)
            # user=models.Message.objects.get(Q(Sender=sender, Receiver=receiver)|Q(Sender=receiver, Receiver=sender))
            user=models.Message.objects.filter(Q(Sender=sender, Receiver=receiver)).values()
        except models.Message.DoesNotExist:
            raise BadRequest("Invalid...")

        # data = messageSerializer(user)
        data = list(user)

        return JsonResponse(data, safe=False)

    else:
        return JsonResponse('Failed to get user data...', safe=False)

# @csrf_exempt
def getDetailMessages(request, sender=None, receiver=None):
    if request.method=="GET":
        try:
            # user=models.Message.objects.get(Sender=sender, Receiver=receiver)
            # user=models.Message.objects.get(Q(Sender=sender, Receiver=receiver)|Q(Sender=receiver, Receiver=sender))
            user=models.Message.objects.filter(Q(Sender=sender, Receiver=receiver)|Q(Sender=receiver, Receiver=sender)).values()
        except models.Message.DoesNotExist:
            raise BadRequest("Invalid...")

        # data = messageSerializer(user)
        data = list(user)

        return JsonResponse(data, safe=False)

    else:
        return JsonResponse('Failed to get user data...', safe=False)
def getImageProduct(request, product_id=None):
    if request.method=="GET":
        try:
            # user=models.Message.objects.get(Sender=sender, Receiver=receiver)
            # user=models.Message.objects.get(Q(Sender=sender, Receiver=receiver)|Q(Sender=receiver, Receiver=sender))
            user=models.imageProduct.objects.filter(product_id=product_id).values()
        except models.imageProduct.DoesNotExist:
            raise BadRequest("Invalid...")

        # data = messageSerializer(user)
        data = list(user)

        return JsonResponse(data, safe=False)

    else:
        return JsonResponse('Failed to get user data...', safe=False)