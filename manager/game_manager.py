"""
creating class GameManager for code realisation
"""
from model.board_game import BoardGame
from model.card_game import CardGame
from model.classic_board_game import ClassicBoardGame
from model.computer_game import ComputerGame
from model.game import Game


class GameManager:
    """
    creating class GameManager
    """

    def __init__(self, list_of_games):
        self.list_of_games = list_of_games

    def find_all_with_release_date_later_than(self, release_date):
        """
        function for finding objects with release date later than the specified one
        """
        return filter(lambda x: x.release_date > release_date, self.list_of_games)

    def find_all_with_max_players_more_than(self, max_players):
        """
        function for finding objects with the maximum of players more than ...
        """
        return filter(lambda x: x.max_players > max_players, self.list_of_games)

    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def get_the_publishers(self):
        # publishers = []
        # for x in self.games:
        #   publishers.append(x.name)
        # return publishers
        return [x.publisher for x in self.games]

    def my_enumerate(self):
        return enumerate(self.games)

    def my_zip(self):
        return zip(self.games, self.get_the_publishers())

    def to_dict(self, data_type):
        # results = []
        # for x in self.list_of_games:
        #   res = {}
        #   for (key, value) in x.__dict__.items():
        #     if type(value) is data_type:
        #       res[key] = value
        #   results.append(res)
        # return results
        return [{key: value for (key, value) in x.__dict__.items() if type(value) is data_type} for x in self.games]

    def run_validation(self, check):
        return {
            'all': all(map(check, self.games)),
            'any': any(map(check, self.games)),
        }

    def __len__(self):
        return len(self.games)

    def __iter__(self):
        return iter(self.games)

    def __getitem__(self, item):
        return self.games[item]






