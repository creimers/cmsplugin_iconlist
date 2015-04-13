# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_iconlist', '0002_auto_20150413_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='icon',
            field=models.CharField(choices=[('fa-facebook', 'facebook'), ('fa-foursquare', 'foursquare')], max_length=200, verbose_name='icon'),
            preserve_default=True,
        ),
    ]
