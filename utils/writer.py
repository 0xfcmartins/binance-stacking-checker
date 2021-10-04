import sys

from datetime import datetime
from env.config import LOG_FORMAT


def init_log():
    sys.stdout = Logger()


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("report/" + datetime.now().strftime(LOG_FORMAT) + ".log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
