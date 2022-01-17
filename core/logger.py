from core.colors import *
from datetime import datetime


class Logger:
    """
    Logger module to log all the happening stuff.
    """
    # Information level logging.
    @classmethod
    def info(self, text):
        print("["+Y+datetime.now().strftime("%H:%M:%S")+N+"] ["+G+"INFO"+N+"] "+text)

    # warning level logging.
    @classmethod
    def warning(self, text):
        print("["+Y+datetime.now().strftime("%H:%M:%S") +
              N+"] ["+Y+"WARNING"+N+"] "+text)

    # error level logging if get any error.
    @classmethod
    def error(self, text):
        print("["+Y+datetime.now().strftime("%H:%M:%S") +
              N+"] ["+R+"ERROR"+N+"] "+text)
