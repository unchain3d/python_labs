from model.Game import Game


class ComputerGame(Game):
    def __init__(self, free_disk_space, genre, metacritic_score):
        self.free_disk_space = free_disk_space
        self.genre = genre
        self.metacritic_score = metacritic_score

    def __str__(self):
        return "Free disk space : % s\n" \
            "Genre : % s\n" \
            "Metacritic score : % s\n" % \
            (self.free_disk_space, self.genre, self.metacritic_score)