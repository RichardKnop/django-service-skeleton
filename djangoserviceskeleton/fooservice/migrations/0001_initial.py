# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'fooservice_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=254)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal(u'fooservice', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'fooservice_user')


    models = {
        u'fooservice.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        }
    }

    complete_apps = ['fooservice']