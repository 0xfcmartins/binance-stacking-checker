import decimal
import time
import requests

from datetime import datetime

from env.config import API_PUBLIC
from env.config import TS_FORMAT
from env.config import INTERVAL
from env.config import Colors

from utils.writer import log


def check(asset):
    response = requests.request("GET", API_PUBLIC + "pageSize=1&pageIndex=1&status=ALL&asset=" + asset)
    projects = response.json()['data'][0]['projects']

    for project in projects:
        is_sold_out = project['sellOut']
        up_limit = decimal.Decimal(project['upLimit'])
        purchased = decimal.Decimal(project['purchased'])

        asset = '{:5}'.format(f"{Colors.ASSET}" + project['asset'] + f"{Colors.END}")
        stack_duration = "for " + f"{Colors.DURATION}" + project['duration'] + f"{Colors.END}" + " days stacking"
        time_stamp = f"{Colors.WARNING}" + datetime.now().strftime(TS_FORMAT) + f"{Colors.END}"
        open_tag = "its " + f"{Colors.TAG}OPEN" + f"{Colors.END}!"

        remaining_calc = f"{Colors.VALUES}" + str(up_limit - purchased) + f"{Colors.END}"

        on_sale = 'Sale:' + f"{Colors.VALUES}" + project['upLimit'] + f"{Colors.END}"
        sold = ' Sold:' + f"{Colors.VALUES}" + project['purchased'] + f"{Colors.END}"
        remaining = ' Remaining:' + remaining_calc

        if not is_sold_out:
            print(time_stamp, asset, stack_duration, open_tag, on_sale, sold, remaining)


def run():
    while 1:
        check("DOT")
        check("SAND")
        check("ONE")
        check("ADA")
        print()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    log()
    run()
