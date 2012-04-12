from pingpong.models import Player
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        for player in Player.objects.all():
            player.bonus_pool += 5
            player.save()