from model.BoardGame import BoardGame
from model.CardGame import CardGame
from model.ClassicBoardGame import ClassicBoardGame
from model.ComputerGame import ComputerGame
from model.Game import Game


class GameManager:
    def __init__(self):
        pass

    def find_all_with_release_date_later_than(self):
        something = list(filter(lambda x: x > 2015, list))
        print(something)

    def find_all_with_max_players_more_than(self):
        something2 = list(filter(lambda x: x > 4, list))
        print(something2)



#testing of Game class
game1 = Game ("Electronic Arts", 2010)
game2 = Game ("FromSoftware", 2022)


#testing of ComputerGame class
computer_game1 = ComputerGame(5000, "horror", 87)
computer_game2 = ComputerGame(8000, "shooter", 79)


#testing of BoardGame class
board_game1 = BoardGame("Amnesia", 2, 4)
board_game2 = BoardGame("Monopoly", 2, 8)
board_game3 = BoardGame("Clue", 1, 4)
board_game4 = BoardGame("Scrabble", 2, 4)
board_game5 = BoardGame("Chess", 2, 2)

print(board_game1.can_play())  # False

board_game1.connect_player()
print(board_game1.can_play())  # False

board_game1.connect_player()
print(board_game1.can_play())  # True

board_game1.disconnect_player()
print(board_game1.can_play())  # True


#testing of ClassicBoardGame class
classic_board_game1 = ClassicBoardGame(30)
classic_board_game2 = ClassicBoardGame(40)


#testing of CardGame class
card_game1 = CardGame(52)
card_game2 = CardGame(54)


#list testing

list = []

list.append(ComputerGame(5000, "horror", 87))
list.append(ComputerGame(8000, "shooter", 79))
list.append(Game("Electronic Arts", 2022))
list.append(Game("FromSoftware", 2022))
list.append(BoardGame("Amnesia", 2, 4))
list.append(BoardGame("Monopoly", 2, 8))
list.append(BoardGame("Clue", 1, 4))
list.append(BoardGame("Scrabble", 2, 4))
list.append(BoardGame("Chess", 2, 2))
list.append(ClassicBoardGame(30))
list.append(ClassicBoardGame(40))
list.append(CardGame(52))
list.append(CardGame(54))

print(*list, sep="\n")