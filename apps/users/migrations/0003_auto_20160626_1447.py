# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160602_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(choices=[('Others', 'Others'), ('Male', 'Male'), ('Female', 'Female')], max_length=8),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.ImageField(upload_to='User/Profile Picture'),
        ),
    ]
