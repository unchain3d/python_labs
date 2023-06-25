import logging


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
