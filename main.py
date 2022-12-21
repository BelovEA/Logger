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
        "если директория path не существует, тогда создаём"
        if path != "./":
            if not os.path.dirname(path):
                os.makedirs(f"./{path}")
        with open(f"{path}log_{Logger.day}.{Logger.month}.{Logger.year}.log", "w"):
            pass


    @classmethod
    def fill_date(self):
        current_date = datetime.datetime.now()
        Logger.day = current_date.day
        Logger.month = current_date.month
        Logger.year = current_date.year
        Logger.hour = current_date.hour
        Logger.minute = current_date.minute
        Logger.second = current_date.second

l = Logger("Logs")

