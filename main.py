import json

from entities.player import Player
from scoring_engine.game import Game

from utils.log import Log
log = Log.getLogger(__name__)


def write_players_score(game):
    file1 = open("player_score.txt", "w")
    file2 = open("player_events.txt", "w")
    file3 = open("tournamet_events.txt", "w")
    player_score = {}
    player_events = {}
    for player in game.players:
        player_score[player.name] = player.total_score
        player_events[player.name] =  player.score_array
    file3.write(json.dumps(game.tournament_event))
    file1.write(json.dumps(player_score))
    file2.write(json.dumps(player_events))

if __name__ == '__main__':
    log.info('Setting up players for the tournament')
    p1 = Player(
        name='Roger Fed',
        total_score = 0,
        score_array = [],
        atp_ranking = -1,
        credits_needed = -1
    )
    p2 = Player(
        name='Novak',
        total_score = 0,
        score_array = [],
        atp_ranking = -1,
        credits_needed = -1
    )
    p3 = Player(
        name='nadal',
        total_score = 0,
        score_array = [],
        atp_ranking = -1,
        credits_needed = -1
    )
    p4 = Player(
        name='Peng sui',
        total_score = 0,
        score_array = [],
        atp_ranking = -1,
        credits_needed = -1
    )
    players = [p1, p2, p3, p4]
    game = Game(players)
    while len(game.current_players_in_game) != 1:
        game.run_round()
    write_players_score (game)

