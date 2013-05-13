# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'University'
        db.create_table(u'nerdeez_backend_app_university', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 13, 0, 0))),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 13, 0, 0), auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=1000, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(default='', max_length=250, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(default='', max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'nerdeez_backend_app', ['University'])


    def backwards(self, orm):
        # Deleting model 'University'
        db.delete_table(u'nerdeez_backend_app_university')


    models = {
        u'nerdeez_backend_app.university': {
            'Meta': {'object_name': 'University'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 13, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 13, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nerdeez_backend_app']