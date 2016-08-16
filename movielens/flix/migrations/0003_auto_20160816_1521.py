# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 20:21
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import migrations


def connect_users_to_raters(apps, schema_editor):
    Rater = apps.get_model('flix', 'Rater')
    User = get_user_model()

    for rater in Rater.objects.all():
        temp_user = User.objects.create_user(
            username='username{}'.format(rater.id),
            email='{}@flix.com'.format(rater.id),
            password='password')
        rater.user_id = temp_user.id
        rater.save()


class Migration(migrations.Migration):

    dependencies = [
        ('flix', '0002_auto_20160816_1420'),
    ]

    operations = [
        migrations.RunPython(connect_users_to_raters)
    ]
