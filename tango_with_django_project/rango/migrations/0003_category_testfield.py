# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170907_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='testField',
            field=models.CharField(default=b'NULL', max_length=128),
            preserve_default=True,
        ),
    ]
