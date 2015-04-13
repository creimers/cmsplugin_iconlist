# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('icon', models.CharField(choices=[('fa-facebook', 'facebook'), ('fa-foursquare', 'foursquare')], verbose_name='icon', max_length=200)),
                ('color', models.CharField(verbose_name='icon color', max_length=200, default='#000000')),
                ('background_color', models.CharField(verbose_name='background color', max_length=200, default='#ffffff')),
                ('link', models.URLField(verbose_name='link')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IconList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=32, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='icon',
            name='icon_list',
            field=models.ForeignKey(to='cmsplugin_iconlist.IconList', related_name='associated_item'),
            preserve_default=True,
        ),
    ]
