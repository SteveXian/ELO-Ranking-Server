from models import Player
import math

K = 32

def update(POST):
    player_one = Player.objects.get(pk=int(POST['player_one']))
    player_one_score = int(POST['player_one_score'])
    player_two = Player.objects.get(pk=int(POST['player_two']))
    player_two_score = int(POST['player_two_score'])
    total_games = player_two_score + player_one_score

    expected_one = get_Expected_A(player_one.ELO, player_two.ELO)
    expected_two = get_Expected_A(player_two.ELO, player_one.ELO)

    player_one.wins += player_one_score
    player_one.losses += player_two_score
    player_one.ELO = update_elo(player_one.ELO, player_one_score, expected_one*total_games)
    player_one.save()

    player_two.wins += player_two_score
    player_two.losses += player_one_score
    player_two.ELO = update_elo(player_two.ELO, player_two_score, expected_two*total_games)
    player_two.save()

def get_Expected_A(Real_A, Real_B):
    return float(1)/( 1 + math.pow(10, ((Real_B - Real_A)/400)))

def update_elo(ELO, Score, Expected):
    return math.ceil(ELO + K*(Score - Expected))