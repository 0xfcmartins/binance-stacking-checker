# -*- coding: utf-8 -*-

"""
    Binance stacking projects availability checker
    @author Francisco Martins francisco.drive.7@gmail.com
"""

import decimal
import time
import requests
import os

from datetime import datetime
from requests import RequestException

from utils.colors import API_PUBLIC
from utils.colors import TS_FORMAT
from utils.colors import INTERVAL
from utils.colors import Colors
from utils.colors import duration_color

from utils.writer import init_log

from utils.sms import notify, telegram

phone = '<user_notification_number>'


def check(asset):
    try:
        response = requests.request("GET", API_PUBLIC + "pageSize=1&pageIndex=1&status=ALL&asset=" + asset)
        for data in response.json()['data']:
            for project in data['projects']:
                is_sold_out = project['sellOut']
                up_limit = decimal.Decimal(project['upLimit'])
                purchased = decimal.Decimal(project['purchased'])
                duration = project['duration']

                stack_duration = "for " + duration_color(duration, duration) + " days stacking"
                asset = '{:5}'.format(f"{Colors.ASSET}" + project['asset'] + f"{Colors.END}")
                time_stamp = f"{Colors.WARNING}" + datetime.now().strftime(TS_FORMAT) + f"{Colors.END}"
                open_tag = "its " + f"{Colors.TAG}OPEN" + f"{Colors.END}!"

                remaining_calc = f"{Colors.VALUES}" + str(up_limit - purchased) + f"{Colors.END}"

                on_sale = 'Sale:' + f"{Colors.VALUES}" + project['upLimit'] + f"{Colors.END}"
                sold = ' Sold:' + f"{Colors.VALUES}" + project['purchased'] + f"{Colors.END}"
                remaining = ' Remaining:' + remaining_calc

                if not is_sold_out:
                    print(time_stamp, asset, stack_duration, open_tag, on_sale, sold, remaining)
                    if duration == '90' or duration == '60':
                        notify(asset, duration, phone)
                    telegram(asset, duration)

    except RequestException as e:
        print(e)
        time.sleep(120)


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def run(check_assets):
    while True:
        try:
            for i in check_assets.split(" "):
                check(i)

            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    global phone_number

    print("Input the assets tags separated by space:")
    assets = input()

    clear()
    init_log()
    run(assets)
