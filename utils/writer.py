import sys
import os

from datetime import datetime
from utils.colors import LOG_FORMAT, Colors


def validate_folder():
    path = "report"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the reports directory %s failed" % path)


def init_log():
    validate_folder()
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
