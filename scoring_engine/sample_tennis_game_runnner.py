from entities.player import Player
import random
from utils.log import Log
log = Log.getLogger(__name__)

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
        self.match_ended = False
        self.fantasy_score_map = {
            'POINT_WIN': 1,
            'GAME_WIN': 1,
            'ACE_SERVE': 1,
            'SET_WIN': 1,
            'MATCH_WIN': 1
        }
        self.set_score = {
            1: 0,
            2: 0,
        }
        self.match_score = {
            1: 0,
            2: 0,
        }

    def player1_scores(self, randomise_ace = True):
        if self.match_ended:
           log.info("Game ended Return")
        self.count_fanatasy_score_for_player_for_event(player= self.player1, event='POINT_WIN')
        if randomise_ace:
            random_chance = self.ace_serve_randomness()
            if random_chance:
                self.count_fanatasy_score_for_player_for_event(player=self.player1, event='ACE_SERVE')
        self.player1_score += 1
        self.get_score()

    def player2_scores(self, randomise_ace = True):
        if self.match_ended:
           log.info("Game ended Return")
        self.count_fanatasy_score_for_player_for_event(player=self.player2, event='POINT_WIN')
        if randomise_ace:
            random_chance = self.ace_serve_randomness()
            if random_chance:
                self.count_fanatasy_score_for_player_for_event(player=self.player2, event='ACE_SERVE')
        self.player2_score += 1
        self.get_score()

    def count_fanatasy_score_for_player_for_event(self, event = None, player = None):
        player.score_array.append((event, self.fantasy_score_map[event]))
        player.total_score += self.fantasy_score_map[event]

    def ace_serve_randomness(self):
        random_num = random.randint(0, 11)
        random_chance = True if random_num >= 10 else False
        return random_chance

    def is_game_ended(self):
        return self.match_ended

    def initialise_game_score(self):
        self.player1_score = 0
        self.player2_score = 0

    def initialise_set_score(self):
        self.initialise_game_score()
        self.set_score = {
            1: 0,
            2: 0,
        }

    def get_score(self):
        score_map = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        log.info(score_map.get(self.player1_score, f"Game-{self.player1_score}") + "-" + score_map.get(self.player2_score, f"Game-{self.player1_score}"))
        if self.player1_score >= 3 or self.player2_score >= 3:
            if self.player1_score == self.player2_score:
                log.info( f"{self.player1.name} - {self.player2.name}  Deuce" )
            elif self.player1_score - self.player2_score == 1:
                log.info( "Advantage " + self.player1_name)
            elif self.player2_score - self.player1_score == 1:
                log.info("Advantage " + self.player2_name)
            elif self.player1_score - self.player2_score >= 2:
                log.info( self.player1_name + " wins the set")
                self.count_set_point()
            elif self.player2_score - self.player1_score >= 2:
                log.info( self.player2_name + " wins the set")
                self.count_set_point()


    def count_set_point(self):
        if self.player1_score > self.player2_score:
            self.count_fanatasy_score_for_player_for_event(player=self.player1, event='SET_WIN')
            self.set_score[1] += 1
            self.initialise_game_score()
        else:
            self.count_fanatasy_score_for_player_for_event(player=self.player2, event='SET_WIN')
            self.set_score[2] += 1
            self.initialise_game_score()
        self.check_for_set_finish()
        self.check_for_game_finish()

    def check_for_set_finish(self):
        if self.set_score[1] >= 6 or  self.set_score[2] >= 6 :
            if self.set_score[1] - self.set_score[2] >= 2:
                self.count_fanatasy_score_for_player_for_event(player=self.player1, event='GAME_WIN')
                self.match_score[1] += 1
                self.initialise_set_score()
            elif self.set_score[2] - self.set_score[1] >= 2:
                self.count_fanatasy_score_for_player_for_event(player=self.player2, event='GAME_WIN')
                self.match_score[2] += 1
                self.initialise_set_score()
            elif self.set_score[1] == 7:
                self.count_fanatasy_score_for_player_for_event(player=self.player1, event='GAME_WIN')
                self.match_score[1] += 1
                self.initialise_set_score()
            elif self.set_score[2] == 7:
                self.count_fanatasy_score_for_player_for_event(player=self.player2, event='GAME_WIN')
                self.match_score[2] += 1
                self.initialise_set_score()

    def check_for_game_finish(self):
            if self.match_score[1] >= 2 or self.match_score[2] >= 2:
                if self.match_score[1] - self.match_score[2] == 2 or self.match_score[1] == 3:
                    self.count_fanatasy_score_for_player_for_event(player=self.player1, event='MATCH_WIN')
                    self.winner = self.player1
                    self.loser = self.player2
                    log.info(f"Match finished. Winner : {self.winner.name}  loser : {self.loser.name}")
                    log.info(
                        f"p1: {self.player1.name} p2 : {self.player2.name} ms : {self.match_score}, ss: {self.set_score} gs : {self.player1_score} - {self.player2_score}")
                    self.match_ended = True
                elif self.match_score[2] - self.match_score[1] == 2 or self.match_score[2] == 3:
                    self.count_fanatasy_score_for_player_for_event(player=self.player2, event='MATCH_WIN')
                    self.winner = self.player2
                    self.loser = self.player1
                    log.info(f"Match finished. Winner : {self.winner.name}  loser : {self.loser.name}")
                    log.info(
                        f"p1: {self.player1.name} p2 : {self.player2.name} , ms : {self.match_score}, ss: {self.set_score} gs : {self.player1_score} - {self.player2_score}")
                    self.match_ended = True
                else:
                    log.info(f"More game need to be played, ms : {self.match_score}, ss: {self.set_score} gs : {self.player1_score} - {self.player2_score}" )
            else:
                log.info( f"More game need to be played, ms : {self.match_score}, ss: {self.set_score} gs : {self.player1_score} - {self.player2_score}")




