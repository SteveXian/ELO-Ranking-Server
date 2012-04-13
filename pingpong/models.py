from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=200)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ELO = models.IntegerField()
    bonus_pool = models.IntegerField(null=False)

    def __unicode__(self):
        return """%s
        wins: %s
        losses: %s
        ELO: %s
        bonus_pool: %s """ % (self.player_name, self.wins, self.losses, self.ELO, self.bonus_pool)

class Record(models.Model):
    date = models.DateTimeField(auto_now=False);
    player_one_id = models.IntegerField()
    player_one_score = models.IntegerField()
    player_two_id = models.IntegerField()
    player_two_score = models.IntegerField()

    def __unicode__(self):
        return """%s
        player_one: %s
        player_one_score: %s
        player_two: %s
        player_two_score: %s """ % (self.date, self.player_one_id, self.player_one_score, self.player_two_id, self.player_two_score)

