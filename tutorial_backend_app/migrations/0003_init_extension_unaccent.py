# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.execute(
                   '''
                   CREATE EXTENSION unaccent;
                    ALTER FUNCTION unaccent(text) IMMUTABLE;
                   '''
                   )

    def backwards(self, orm):
        db.execute(
                   '''
                   DROP EXTENSION unaccent;
                   DROP FUNCTION unaccent;
                   '''
                   )

    models = {
        u'nerdeez_backend_app.university': {
            'Meta': {'object_name': 'University'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 20, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 20, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nerdeez_backend_app']