from typing import List

from entities.player import Player
from scoring_engine.sample_tennis_game_runnner import TennisGame
from utils.log import Log
log = Log.getLogger(__name__)

class Game:
    def __init__(self, players: List[Player]) :
        self.players = players
        self.current_players_in_game = players
        self.score_map = {
            'POINT_WIN': 1,
            'GAME_WIN': 1,
            'ACE_SERVE': 1,
            'SET_WIN': 1
        }

    def _draw_pools(self, players: List[Player]) -> List[tuple]:
        if len(players)%2 != 0:
            raise Exception ("Total players should be a multple of 2")
        player_draws = []
        current_pool = []
        for player in players:
            if len(current_pool) < 2:
                current_pool.append(player)
            if len(current_pool) == 2:
                player_draws.append((current_pool[0], current_pool[1]))
                current_pool = []
        return player_draws

    def run_round(self):
        round_pools = self._draw_pools(self.current_players_in_game)
        log.info(f"Starting round with draw pool: {round_pools}")
        players_advancing_to_next_round = []
        for pool in round_pools:
            winner, loser = self.play_game(pool)

    def play_game(self, pool: tuple)-> (Player, Player):
        if len(pool) < 2:
            raise Exception("Cannot play game as there are more than two players")
        p1:Player = pool[0]
        p2:Player = pool[1]
        tennis_game = TennisGame(p1.name, p2.name)





