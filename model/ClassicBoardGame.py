from model.Game import Game


class ClassicBoardGame(Game):
    def __init__(self, average_length):
        self.average_length = average_length
    def __str__(self):
        return "Average length : % s\n" % \
        (self.average_length)