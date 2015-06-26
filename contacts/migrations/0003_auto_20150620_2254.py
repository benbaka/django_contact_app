# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20150610_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='school',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
