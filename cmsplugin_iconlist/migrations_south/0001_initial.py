# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IconList'
        db.create_table(u'cmsplugin_iconlist_iconlist', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_iconlist', ['IconList'])

        # Adding model 'Icon'
        db.create_table(u'cmsplugin_iconlist_icon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('icon_list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='associated_item', to=orm['cmsplugin_iconlist.IconList'])),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('color', self.gf('django.db.models.fields.CharField')(default='#000000', max_length=200)),
            ('background_color', self.gf('django.db.models.fields.CharField')(default='#ffffff', max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'cmsplugin_iconlist', ['Icon'])


    def backwards(self, orm):
        # Deleting model 'IconList'
        db.delete_table(u'cmsplugin_iconlist_iconlist')

        # Deleting model 'Icon'
        db.delete_table(u'cmsplugin_iconlist_icon')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'cmsplugin_iconlist.icon': {
            'Meta': {'object_name': 'Icon'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '200'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'#000000'", 'max_length': '200'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'icon_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'associated_item'", 'to': u"orm['cmsplugin_iconlist.IconList']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'cmsplugin_iconlist.iconlist': {
            'Meta': {'object_name': 'IconList', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_iconlist']