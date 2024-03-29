from django.shortcuts import render_to_response
from django.template import RequestContext
from pingpong.models import Player
import elo

def index(request):
    if request.POST:
        elo.update(request.POST)

    player_list = Player.objects.order_by("ELO").reverse()
    player_list_alpha = Player.objects.order_by("player_name")
    return render_to_response('pingpong/index.html', {'player_list': player_list, 'player_list_alpha':player_list_alpha},
        context_instance=RequestContext(request))
