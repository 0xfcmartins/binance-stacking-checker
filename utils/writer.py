import sys


def log():
    sys.stdout = Logger()


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("report.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
