import logging

class GameIsAlreadyRunningException(Exception):
    pass

def logged(exception, mode):
    def decorator(method):
        def wrapper(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except exception as ex:
                if mode == 'console':
                    logging.error(str(ex))
                elif mode == 'file':
                    logging.basicConfig(filename='logfile.txt', level=logging.ERROR)
                    logging.error(str(ex))
                else:
                    raise ValueError("Недійсний запит. Оберіть 'choose' або 'file")
        return wrapper
    return decorator


class AbstractGame:
    def __init__(self):
        self.progress = 0

    @logged(GameIsAlreadyRunningException, mode='console')
    def play(self):
        if self.progress >= 100:
            raise GameIsAlreadyRunningException("The game is already running.")
        else:
            while self.progress < 100:
                self.progress += 1
                print("Loading... Current progress:", self.progress)


game = AbstractGame()

game.play()  # При першому виклику методу play винятків не виникає

game.play()  # GameIsAlreadyRunningException піднята і залогована в консоль
