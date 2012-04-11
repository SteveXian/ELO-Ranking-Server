from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=200)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ELO = models.IntegerField()

    def __unicode__(self):
        return self.player_name