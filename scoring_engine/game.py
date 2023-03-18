import random
from typing import List

from entities.player import Player
from scoring_engine.sample_tennis_game_runnner import TennisGame
from utils.log import Log
log = Log.getLogger(__name__)

class Game:
    def __init__(self, players: List[Player]) :
        self.round_id = 0
        self.players = players
        self.current_players_in_game = players
        self.tournament_event = {}

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
        self.round_id += 1
        round_pools = self._draw_pools(self.current_players_in_game)
        log.info(f"Starting round with draw pool: {round_pools}")
        players_advancing_to_next_round = []
        self.match_count = 1
        for pool in round_pools:
            winner, loser = self.play_game(pool)
            players_advancing_to_next_round.append(winner)
            self.tournament_event[f'R-{self.round_id}-M-{self.match_count}'] = {'winner': winner.name, 'loser': loser.name}
            self.match_count += 1
        self.current_players_in_game = players_advancing_to_next_round

    def play_game(self, pool: tuple)-> (Player, Player):
        if len(pool) < 2:
            raise Exception("Cannot play game as there are more than two players")
        p1:Player = pool[0]
        p2:Player = pool[1]
        tennis_game = TennisGame(p1, p2)
        log.info('Starting the game')
        while not tennis_game.is_game_ended():
            rand = random.randint(0, 1)
            if rand == 0:
                tennis_game.player1_scores()
            elif rand == 1:
                tennis_game.player2_scores()
        return tennis_game.winner, tennis_game.loser






