from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, publisher, release_date):
        self.publisher = publisher
        self.release_date = release_date
        self.current_players = 0

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

