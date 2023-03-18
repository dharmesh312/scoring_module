from entities.player import Player


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

    def player1_scores(self):
        self.player1_score += 1

    def player2_scores(self):
        self.player2_score += 1

    def is_game_ended(self):
        return self.game_ended

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
                self.finish_game_and_decide_winner()
                return self.player1_name + " wins"
            elif self.player2_score - self.player1_score >= 2:
                self.finish_game_and_decide_winner()
                return self.player2_name + " wins"
        else:
            return score_map[self.player1_score] + "-" + score_map[self.player2_score]

    def finish_game_and_decide_winner(self):
        self.game_ended = True
        if self.player1_score > self.player2_score:
            self.winner = self.player1
            self.loser = self.player2
        else:
            self.winner = self.player2
            self.loser = self.player1