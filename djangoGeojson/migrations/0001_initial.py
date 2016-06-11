# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
