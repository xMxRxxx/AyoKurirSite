# Generated by Django 3.2.5 on 2022-05-11 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ak_company', '0008_auto_20220509_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(upload_to='media/images/product/'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image1',
            field=models.ImageField(upload_to='media/images/product/'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image2',
            field=models.ImageField(upload_to='media/images/product/'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image3',
            field=models.ImageField(upload_to='media/images/product/'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image4',
            field=models.ImageField(upload_to='media/images/product/'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image5',
            field=models.ImageField(upload_to='media/images/product/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 21, 19, 4, 292282, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofil',
            name='foto',
            field=models.ImageField(upload_to='media/images/profil/user/'),
        ),
        migrations.AlterField(
            model_name='userprofil',
            name='fotoktp_mitra_company',
            field=models.ImageField(default=None, upload_to='media/images/profil/mitra/ktp/'),
        ),
    ]