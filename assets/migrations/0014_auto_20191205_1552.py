# Generated by Django 2.2 on 2019-12-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0013_auto_20191205_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='PrivateIP',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='私网IPV4地址'),
        ),
        migrations.AlterField(
            model_name='server',
            name='PublicIP',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='公网IPV4地址'),
        ),
    ]