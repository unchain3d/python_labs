from model.board_game import BoardGame
from model.card_game import CardGame
from model.classic_board_game import ClassicBoardGame
from model.computer_game import ComputerGame
from model.game import Game
from manager.game_manager import GameManager

if __name__ == "__main__":

    # testing of Game class
    game1 = Game("Electronic Arts", 2010)
    game2 = Game("FromSoftware", 2022)

    # testing of ComputerGame class
    computer_game1 = ComputerGame(5000, "horror", 87)
    computer_game2 = ComputerGame(8000, "shooter", 79)

    # testing of BoardGame class
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

    # testing of ClassicBoardGame class
    classic_board_game1 = ClassicBoardGame(30)
    classic_board_game2 = ClassicBoardGame(40)

    # testing of CardGame class
    card_game1 = CardGame(52)
    card_game2 = CardGame(54)

    list_of_games = GameManager()

    list_of_games.add_game(Game("Electronic Arts", 2022))
    list_of_games.add_game(Game("FromSoftware", 2022))
    list_of_games.add_game(Game("Nintendo", 2012))
    list_of_games.add_game(Game("Activision Blizzard", 2015))
    list_of_games.add_game(Game("SEGA", 1998))

    print(list_of_games.get_the_publishers())
    print(list_of_games.my_enumerate())
    print(list_of_games.my_zip())
    print(list_of_games.to_dict(int))
    print(list_of_games.run_validation(lambda x: x.release_date > 2000))
    example_of_enumeration = list(list_of_games.my_enumerate())
    for i, game in example_of_enumeration:
        print(i, game)
    example_of_zip = list(list(list_of_games.my_zip()))
    for x, game in example_of_zip:
        print(x, game)














