# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flix', '0007_rating_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='review',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
