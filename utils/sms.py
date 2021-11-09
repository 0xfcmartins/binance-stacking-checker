import requests
import hashlib

from utils.writer import replacer

# noinspection SpellCheckingInspection
bot_token = ''
telegram_base = 'https://api.telegram.org/bot'
pro_mode = ''
dev_key = 'textbelt'
chat_id = ''
sent = {}


def notify(asset, duration, phone_number):
    global sent

    message = '🚨🚨 ' + replacer(asset) + ' 🚨🚨 is OPEN ' + replacer(duration) + ' days on Binance!'
    if hashlib.md5(message.encode()).hexdigest() not in sent:
        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': message + ' OPEN on binance!',
            'key': pro_mode
        })
        if resp.json()['success'] == 'False':
            print('SMS notification sent!')

        sent[hashlib.md5(message.encode()).hexdigest()] = True


def telegram(asset, duration):
    message = '🚨🚨 ' + replacer(asset) + ' 🚨🚨 is OPEN ' + replacer(duration) + ' days on Binance!'
    send_text = telegram_base + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message
    requests.get(send_text)
