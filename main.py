from entities.player import Player
from scoring_engine.game import Game

from utils.log import Log
log = Log.getLogger(__name__)

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
    game.run_round()