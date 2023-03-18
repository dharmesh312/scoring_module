from entities.player import Player
import random

class TennisGame:
    def __init__(self, player1, player2):
        self.player1: Player = player1
        self.player2: Player = player2
        self.player1_name = player1.name
        self.player2_name = player2.name
        self.player1_score = 0
        self.player2_score = 0
        self.winner = None
        self.loser = None
        self.game_ended = False
        self.fantasy_score_map = {
            'POINT_WIN': 1,
            'GAME_WIN': 1,
            'ACE_SERVE': 1,
            'SET_WIN': 1
        }
        self.set_winner = []

    def player1_scores(self, randomise_ace = True):
        self.count_fanatasy_score_for_player_for_event(player= self.player1, event='POINT_WIN')
        if randomise_ace:
            random_chance = self.ace_serve_randomness()
            if random_chance:
                self.count_fanatasy_score_for_player_for_event(player=self.player1, event='ACE_SERVE')
        self.player1_score += 1

    def player2_scores(self, randomise_ace = True):
        self.count_fanatasy_score_for_player_for_event(player=self.player2, event='POINT_WIN')
        if randomise_ace:
            random_chance = self.ace_serve_randomness()
            if random_chance:
                self.count_fanatasy_score_for_player_for_event(player=self.player2, event='ACE_SERVE')
        self.player2_score += 1

    def count_fanatasy_score_for_player_for_event(self, event = None, player = None):
        player.score_array.append((event, self.fantasy_score_map[event]))
        player.total_score += self.fantasy_score_map[event]

    def ace_serve_randomness(self):
        random_num = random.randint(0, 11)
        random_chance = True if random_num >= 10 else False
        return random_chance

    def is_game_ended(self):
        return self.game_ended

    def initialise_set(self):
        self.player1_score = 0
        self.player2_score = 0

    def get_score(self):
        score_map = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

        if self.player1_score >= 3 and self.player2_score >= 3:
            if self.player1_score == self.player2_score:
                return "Deuce"
            elif self.player1_score - self.player2_score == 1:
                return "Advantage " + self.player1_name
            elif self.player2_score - self.player1_score == 1:
                return "Advantage " + self.player2_name
            elif self.player1_score - self.player2_score >= 2:
                self.finish_set_and_decide_winner()
                return self.player1_name + " wins"
            elif self.player2_score - self.player1_score >= 2:
                self.finish_set_and_decide_winner()
                return self.player2_name + " wins"
        else:
            return score_map[self.player1_score] + "-" + score_map[self.player2_score]

    def finish_set_and_decide_winner(self):
        if self.player1_score > self.player2_score:
            self.count_fanatasy_score_for_player_for_event(player=self.player1, event='SET_WIN')
            self.set_winner.append(1)
            self.initialise_set()
        else:
            self.count_fanatasy_score_for_player_for_event(player=self.player2, event='SET_WIN')
            self.set_winner.append(2)
            self.initialise_set()

    def check_for_game_finish(self):
        if len(self.set_winner) < 2:
            return
        if len(self.set_winner) >= 2:
            if self.set_winner.count(1) >= 2:
                self.winner = self.player1
                self.loser = self.player2
            elif self.set_winner.count(2) >= 2:
                self.winner = self.player2
                self.loser = self.player1
            self.game_ended = True
