# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_contact_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=40)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
