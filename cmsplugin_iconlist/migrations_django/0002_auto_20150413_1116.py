# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_iconlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='icon',
            field=models.CharField(max_length=200, choices=[('fa-facebook', 'facebook'), ('fa-foursquare', 'foursquare')], verbose_name='icon color'),
            preserve_default=True,
        ),
    ]
