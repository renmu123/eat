# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-25 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat', '0006_post_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='average',
            field=models.IntegerField(default=10),
        ),
    ]