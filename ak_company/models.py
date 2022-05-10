from distutils.command.upload import upload
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.dispatch import receiver
from django.utils import timezone

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your models here.
tipePengguna = (
    ('K', 'kurir'),
    ('C', 'kedai'),
    ('U', 'umum')
)
CATEGORY_CHOICES = (
    ('M', 'makanan'),
    ('P', 'pakaian'),
    ('A', 'aksesoris'),
    ('SB', 'sayur dan buah - buahan'),
    ('ART', 'alat rumah tangga'),
)

LABEL_CHOICES = (
    ('H', 'hot'),
    ('T', 'terbaru'),
    ('P', 'populer'),
    
)

class userProfil(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    nomortelepon = models.IntegerField(default=0)
    alamat = models.CharField(max_length=100)
    tgllahir = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    foto = models.ImageField(upload_to="images/profil/user/")
    nik_mitra_company = models.IntegerField(default=0)
    fotoktp_mitra_company = models.ImageField(upload_to="images/profil/mitra/ktp/", default=None)
    tipeUser = models.CharField(choices=tipePengguna, max_length=3, default=tipePengguna[2][1])
    status = models.BooleanField(default=False)
    coordinat_sekarang = models.CharField(max_length=10000000)
    def __str__(self):
        return self.username




class Message(models.Model): # many-to-many intermediate table
    ID = models.AutoField(primary_key=True) #This is an auto-incrementing primary key.
    Sender = models.ForeignKey(userProfil, on_delete = models.CASCADE, null=False, related_name="ofMessageUser")
    Receiver = models.ForeignKey(userProfil, on_delete = models.CASCADE, null=False, related_name="toMessageUser")
    # IdentifierNumber = models.IntegerField() #unique for all user
    Content=models.CharField(null=False, max_length=4096,) #Like Telegram limit
    CONTENT_TYPE_CHOICES = ( 
        ("Text", "Text"), 
        ("Image", "Image"), 
        ("Audio", "Audio"), 
        ("Video", "Video") 
    )
    Type = models.CharField(null=False, choices=CONTENT_TYPE_CHOICES, max_length=5, default="Text")
    Date = models.DateTimeField(null=False, default=timezone.now()) #default server timezone -> Europe/London


    
class Item(models.Model):
    username = models.ForeignKey(userProfil,
                             on_delete=models.CASCADE)
    product_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })
        
class imageProduct(models.Model):
    product_id = models.ForeignKey(Item,
                             on_delete=models.CASCADE) 
    image = models.ImageField(upload_to="images/product/")
    image1 = models.ImageField(upload_to="images/product/")
    image2 = models.ImageField(upload_to="images/product/")
    image3 = models.ImageField(upload_to="images/product/")
    image4 = models.ImageField(upload_to="images/product/")
    image5 = models.ImageField(upload_to="images/product/")
    

class favorit(models.Model):
    # user_id = models.ForeignKey(userProfil,on_delete=models.CASCADE)
    username_favorit = models.ForeignKey(userProfil, on_delete=models.CASCADE)
    favorit_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.username_favorit.username
class transaksi(models.Model):
    # user_id = models.ForeignKey(userProfil,on_delete=models.CASCADE)
    username_transaksi = models.ForeignKey(userProfil, on_delete=models.CASCADE)
    name_product = models.ForeignKey(Item,on_delete=models.CASCADE)

class OrderItem(models.Model):
    username = models.ForeignKey(userProfil,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    username = models.ForeignKey(userProfil,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    # shipping_address = models.ForeignKey(
    #     'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    # # billing_address = models.ForeignKey(
    # #     'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    # # payment = models.ForeignKey(
    # #     'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # coupon = models.ForeignKey(
    #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    # being_delivered = models.BooleanField(default=False)
    # received = models.BooleanField(default=False)
    # refund_requested = models.BooleanField(default=False)
    # refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    # def __str__(self):
    #     return self.user.username

    # def get_total(self):
    #     total = 0
    #     for order_item in self.items.all():
    #         total += order_item.get_final_price()
    #     if self.coupon:
    #         total -= self.coupon.amount
    #     return total

# class RequestFriendship(models.Model):
#     ID = models.AutoField(primary_key=True) #This is an auto-incrementing primary key.
#     Receiver = models.ForeignKey("User", on_delete = models.CASCADE, null=False, related_name="toRequestUser")
#     Sender = models.ForeignKey("User", on_delete = models.CASCADE, null=False, related_name="ofRequestUser")

#     class Meta:
#         unique_together = (("Receiver", "Sender"),)
        
# class Message(models.Model): # many-to-many intermediate table
#     ID = models.AutoField(primary_key=True) #This is an auto-incrementing primary key.
#     Sender = models.OneToOneField(userProfil, on_delete = models.CASCADE, null=False, related_name="ofMessageUser")
#     Receiver = models.OneToOneField(userProfil, on_delete = models.CASCADE, null=False, related_name="toMessageUser")
#     IdentifierNumber = models.IntegerField() #unique for all user
#     Content=models.CharField(null=False, max_length=4096,) #Like Telegram limit
#     CONTENT_TYPE_CHOICES = ( 
#         ("Text", "Text"), 
#         ("Image", "Image"), 
#         ("Audio", "Audio"), 
#         ("Video", "Video") 
#     )
#     Type = models.CharField(null=False, choices=CONTENT_TYPE_CHOICES, max_length=5, default="Text")
#     Date = models.DateTimeField(null=False, default=timezone.now()) #default server timezone -> Europe/London
    
    