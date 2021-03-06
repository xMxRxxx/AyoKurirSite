# Generated by Django 4.0.4 on 2022-05-06 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ak_company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofil',
            old_name='namaBelakang',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='userprofil',
            name='namaDepan',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=3)),
                ('label', models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/product/')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ak_company.userprofil')),
            ],
        ),
    ]
