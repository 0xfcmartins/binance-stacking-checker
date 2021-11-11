import json
from types import SimpleNamespace

API_PUBLIC = "https://www.binance.com/bapi/earn/v1/friendly/pos/union?"
TS_FORMAT = "%d/%m/%Y %H:%M:%S"
LOG_FORMAT = "%d%m%Y"
CONFIG_FILE = '../config/config.json'
INTERVAL = 30

app_config_file = None


class Colors:
    ASSET = '\033[96m'
    WARNING = '\033[90m'
    VALUES = '\033[94m'
    TAG = '\033[92m'
    END = '\033[0m'
    R30 = '\033[48;5;12m'
    R60 = '\033[48;5;9m'
    R90 = '\033[48;5;76m'
    R_BG = '\033[38;5;15m'


def bg_color(text, color):
    return "\33[48;5;" + str(color) + "m" + text + "\33[0m"


def duration_color(text, color):
    if color == '30':
        return bg_color("\33[38;5;" + str(15) + "m " + text + " \33[0m", 12)
    elif color == '60':
        return bg_color("\33[38;5;" + str(15) + "m " + text + " \33[0m", 9)
    elif color == '90':
        return bg_color("\33[38;5;" + str(15) + "m " + text + " \33[0m", 76)
    else:
        return "\33[38;5;" + str(color) + "m" + text + "\33[0m"


def load_config():
    file = open(CONFIG_FILE)
    config = json.load(file)
    file.close()

    global app_config_file
    app_config_file = json.loads(json.dumps(config), object_hook=lambda d: SimpleNamespace(**d))
    print(app_config_file.interval)


def get_conf():
    if app_config_file is None:
        load_config()

    return app_config_file


if __name__ == '__main__':
    load_config()

