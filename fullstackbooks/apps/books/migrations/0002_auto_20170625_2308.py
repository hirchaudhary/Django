# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-25 23:08
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='books',
            managers=[
                ('booksManager', django.db.models.manager.Manager()),
            ],
        ),
    ]