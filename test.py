import pandas as pd

import requests
import json

def get_data():
    response = requests.get(url='https://api.binance.com/api/v3/ticker/d?symbol=ETHUSDT')

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file)

if __name__ == '__main__':
    get_data()
