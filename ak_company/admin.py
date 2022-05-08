from django.contrib import admin
from .models import userProfil,Item, Message, OrderItem, Order, imageProduct, favorit, transaksi

# Register your models here.
admin.site.register(userProfil)
admin.site.register(Item)
admin.site.register(Message)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(imageProduct)
admin.site.register(favorit)
admin.site.register(transaksi)