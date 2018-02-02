# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 05:37
from __future__ import unicode_literals

import accounts.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='accounts/default/default.jpg', upload_to=accounts.models.user_path),
        ),
    ]
