import sys

from datetime import datetime
from env.config import LOG_FORMAT, Colors


def init_log():
    sys.stdout = Logger()


def replacer(message):
    for a in dir(Colors):
        if not a.startswith('__'):
            message = message.replace(getattr(Colors, a), '')

    return message


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("report/" + datetime.now().strftime(LOG_FORMAT) + ".log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(replacer(message))
        self.log.flush()

    def flush(self):
        pass
