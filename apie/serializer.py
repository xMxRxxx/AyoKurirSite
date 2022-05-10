from rest_framework import serializers
from ak_company import models

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'product_id',
            'username',
            'title',
            'price',
            'discount_price',
            'category',
            'label',
            'description',
        ]
        model = models.Item

class imageProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
        'product_id',
        'image',
        'image1',
        'image2',
        'image3',
        'image4',
        'image5',

        ]
        model = models.imageProduct



class userSerializer(serializers.ModelSerializer):
    class Meta:
        fields=[
        'user_id',
        'username',
        'nomortelepon',
        'alamat',
        'tgllahir',
        'password',
        'email',
        'foto',
        'nik_mitra_company',
        'fotoktp_mitra_company',
        'tipeUser',
        'status',
        'coordinat_sekarang'
        ]
        model = models.userProfil

# class messageSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = [
#         'ID',
#         'Sender',
#         'Receiver',
#         'Content',
#         'Type',
#         'Date',
#         ]
#         model = models.Message

























