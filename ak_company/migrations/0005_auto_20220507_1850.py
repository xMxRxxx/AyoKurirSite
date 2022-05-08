# Generated by Django 3.2.5 on 2022-05-07 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ak_company', '0004_alter_message_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='requestfriendship',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='requestfriendship',
            name='Receiver',
        ),
        migrations.RemoveField(
            model_name='requestfriendship',
            name='Sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='IdentifierNumber',
        ),
        migrations.RemoveField(
            model_name='userprofil',
            name='Friends',
        ),
        migrations.RemoveField(
            model_name='userprofil',
            name='Messages',
        ),
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 11, 50, 50, 322095, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
        migrations.DeleteModel(
            name='RequestFriendship',
        ),
    ]
