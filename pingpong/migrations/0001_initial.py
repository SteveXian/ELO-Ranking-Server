# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Player'
        db.create_table('pingpong_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('wins', self.gf('django.db.models.fields.IntegerField')()),
            ('losses', self.gf('django.db.models.fields.IntegerField')()),
            ('ELO', self.gf('django.db.models.fields.IntegerField')()),
            ('bonus_pool', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('pingpong', ['Player'])


    def backwards(self, orm):
        
        # Deleting model 'Player'
        db.delete_table('pingpong_player')


    models = {
        'pingpong.player': {
            'ELO': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Player'},
            'bonus_pool': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {}),
            'player_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wins': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['pingpong']
