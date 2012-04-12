from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=200)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ELO = models.IntegerField()
    bonus_pool = models.IntegerField(null=False)

    def __unicode__(self):
        #return self.player_name
        return """%s
        wins: %s
        losses: %s
        ELO: %s
        bonus_pool: %s """ % (self.player_name, self.wins, self.losses, self.ELO, self.bonus_pool)