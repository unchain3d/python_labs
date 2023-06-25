from model.game import Game


class BoardGame(Game):
    def __init__(self, title, min_players, max_players):
        self.title = title
        self.min_players = min_players
        self.max_players = max_players
        self.current_players = 0

    def can_play(self):
        return self.min_players <= self.current_players <= self.max_players

    def __str__(self):
        return "Title : % s\n" \
            "Min_players : % s\n" \
            "Max_players : % s\n" % \
            (self.title, self.min_players, self.max_players)