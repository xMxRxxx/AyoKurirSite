# Generated by Django 4.0.4 on 2022-05-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userProfil',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('namaDepan', models.CharField(max_length=100)),
                ('namaBelakang', models.CharField(max_length=100)),
                ('nomortelepon', models.IntegerField(default=0)),
                ('alamat', models.CharField(max_length=100)),
                ('tgllahir', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.ImageField(upload_to='images/profil/user/')),
                ('nik_mitra_company', models.IntegerField(default=0)),
                ('fotoktp_mitra_company', models.ImageField(upload_to='images/profil/mitra/ktp/')),
                ('tipeUser', models.CharField(choices=[('K', 'kurir'), ('C', 'kedai'), ('U', 'umum')], default='umum', max_length=3)),
            ],
        ),
    ]
