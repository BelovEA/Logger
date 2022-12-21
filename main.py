import os
import datetime




class Logger:
    day = 0
    month = 0
    year = 0
    hour = 0
    minute = 0
    second = 0
    path = ''



    def __init__(self, path="./"):
        Logger.fill_date()
        Logger.path = path
        "если директория path не существует, тогда создаёмб если существует - скипаем команды"
        if path != ".":
            if not os.path.exists(path):
                os.makedirs(f"./{path}")
            Logger.path = f'./{path}'

        with open(f"{path}/log_{Logger.day}.{Logger.month}.{Logger.year}.log", "w"):
            pass

    @staticmethod
    def today():
        current_date = datetime.datetime.now()
        return {'day': current_date.day,
                'month': current_date.month,
                'year': current_date.year,
                'hour': current_date.hour,
                'minutes': current_date.minute,
                'seconds': current_date.second}

    @classmethod
    def fill_date(cls):
        current_date = cls.today()
        cls.day = current_date.get('day')
        cls.month = current_date.get('month')
        cls.year = current_date.get('year')
        cls.hour = current_date.get('hour')
        cls.minute = current_date.get('minute')
        cls.second = current_date.get('second')

l = Logger("Logs")

