# Generated by Django 4.0.4 on 2022-05-07 10:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ak_company', '0002_rename_namabelakang_userprofil_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='userprofil',
            name='Friends',
            field=models.ManyToManyField(related_name='FriendUser', through='ak_company.Friendship', to='ak_company.userprofil'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('IdentifierNumber', models.IntegerField()),
                ('Content', models.CharField(max_length=4096)),
                ('Type', models.CharField(choices=[('Text', 'Text'), ('Image', 'Image'), ('Audio', 'Audio'), ('Video', 'Video')], default='Text', max_length=5)),
                ('Date', models.DateTimeField(default=datetime.datetime(2022, 5, 7, 10, 36, 52, 330008, tzinfo=utc))),
                ('Receiver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='toMessageUser', to='ak_company.userprofil')),
                ('Sender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ofMessageUser', to='ak_company.userprofil')),
            ],
        ),
        migrations.AddField(
            model_name='friendship',
            name='Person1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofFriendUser', to='ak_company.userprofil'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='Person2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toFriendUser', to='ak_company.userprofil'),
        ),
        migrations.AddField(
            model_name='userprofil',
            name='Messages',
            field=models.ManyToManyField(related_name='MessageUser', to='ak_company.message'),
        ),
        migrations.CreateModel(
            name='RequestFriendship',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toRequestUser', to='ak_company.userprofil')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofRequestUser', to='ak_company.userprofil')),
            ],
            options={
                'unique_together': {('Receiver', 'Sender')},
            },
        ),
    ]