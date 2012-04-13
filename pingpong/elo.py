from models import Player, Record
import datetime
import math

K = 16
MAX_BONUS_PER_GAME = 10
#the higher the number, the lower the sensitivity
ELO_SENSITIVITY = 100

def update(POST):
    player_one = Player.objects.get(pk=int(POST['player_one']))
    player_one_score = int(POST['player_one_score'])
    player_two = Player.objects.get(pk=int(POST['player_two']))
    player_two_score = int(POST['player_two_score'])

    record = Record(date=datetime.datetime.now(), player_one_id=player_one.id, player_one_score=player_one_score, player_two_id=player_two.id, player_two_score=player_two_score)
    record.save()

    if player_one.ELO > player_two.ELO:
        expected_one = get_Expected(player_one.ELO, player_two.ELO)
    else:
        expected_one = 1 - get_Expected(player_two.ELO, player_one.ELO)

    update_player(player_one, player_one_score, player_two, player_two_score, expected_one)
    update_player(player_two, player_two_score, player_one, player_one_score, 1-expected_one)

def get_Expected(Real_A, Real_B):
    return 1 - (1/(math.pow(2, ((Real_A - Real_B)/float(ELO_SENSITIVITY)) + 1)))

def update_elo(ELO, Score, Expected):
    return math.ceil(ELO + K*(Score - Expected))

def update_player(player_one, player_one_score, player_two, player_two_score, expected):
    total_games = player_two_score + player_one_score

    player_one.wins += player_one_score
    player_one.losses += player_two_score
    player_one.ELO = update_elo(player_one.ELO, player_one_score, expected*total_games)
    
    if player_one.bonus_pool < MAX_BONUS_PER_GAME * total_games:
        player_one.ELO += player_one.bonus_pool
        player_one.bonus_pool = 0
    else:
        player_one.ELO += MAX_BONUS_PER_GAME * total_games
        player_one.bonus_pool -= MAX_BONUS_PER_GAME * total_games

    player_one.save()