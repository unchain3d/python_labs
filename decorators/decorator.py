import logging
from exceptions.exception import GameIsAlreadyRunningException

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



game10 = AbstractGame()

game10.play()  # При першому виклику методу play винятків не виникає

game10.play()  # GameIsAlreadyRunningException піднята і залогована в консоль
