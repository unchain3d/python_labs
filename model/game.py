from abc import ABC, abstractmethod
import logging
from decorators.decorator import logged
from exceptions.exception import GameIsAlreadyRunningException

class Game(ABC):
    def __init__(self, publisher, release_date):
        self.publisher = publisher
        self.release_date = release_date
        self.current_players = 0

    def __str__(self):
        return f'Game {self.publisher}'

    def __repr__(self):
        return f'Game {self.publisher}'

    def connect_player(self):
        if self.current_players < self.max_players:
            self.current_players += 1
            print("Гравець доданий.")
        else:
            print("Максимальна кількість гравців досягнута.")

    def disconnect_player(self):
        if self.current_players > 0:
            self.current_players -= 1
            print("Гравець видалений.")
        else:
            print("Немає гравців у грі.")

    def __str__(self):
        return "Publisher : % s\n" \
            "Release date : % s\n" \
            "Current players : % s\n" % \
            (self.publisher, self.release_date, self.current_players)

    def __init__(self):
        self.progress = 0

    @logged(GameIsAlreadyRunningException, mode='console')
    def play(self):
        if self.progress >= 100:
            raise GameIsAlreadyRunningException("The game is already running.")
        else:
            while self.progress < 100:
                self.progress += 4
                print("Loading... Current progress:", self.progress)



