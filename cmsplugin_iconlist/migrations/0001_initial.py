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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('icon', models.CharField(choices=[('fa-facebook', 'facebook'), ('fa-foursquare', 'foursquare'), ('fa-google-plus', 'google-plus'), ('fa-instagram', 'instagram'), ('fa-linkedin', 'linkedin'), ('fa-twitter', 'twitter'), ('fa-xing', 'xing'), ('fa-yelp', 'yelp'), ('fa-youtube-play', 'youtube')], max_length=200, verbose_name='icon')),
                ('color', models.CharField(default='#000000', verbose_name='icon color', max_length=200)),
                ('background_color', models.CharField(default='#ffffff', verbose_name='background color', max_length=200)),
                ('link', models.URLField(verbose_name='link')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IconList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='cms.CMSPlugin', primary_key=True)),
                ('name', models.CharField(null=True, blank=True, default='', verbose_name='name', max_length=32)),
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
