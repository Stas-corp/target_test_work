import requests
from apscheduler.schedulers.blocking import BlockingScheduler

sch = BlockingScheduler()

def get_data_symbol(symbol='ETHUSDT') -> dict[str, str]:
    response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}')
    return response.json()

class Percent:
    def __init__(self):
        self.old_price = self.set_was_price()
        self.was_price = None

    def set_was_price(self):
        return float(get_data_symbol()['price'])

    def calculate_percentage(self):
        self.was_price = self.set_was_price()
        percent = round((self.was_price - self.old_price)/self.old_price * 100, 3)
        if abs(percent) > 0.01:
            print(
                f'Regarding the price {self.old_price}\
                Сhange by -> {percent} percent\
                Was price -> {self.was_price}'
                )
            self.old_price = self.was_price
        
task = Percent()
job = sch.add_job(task.calculate_percentage, trigger='interval', seconds=1, max_instances=2)

if __name__ == '__main__':
    sch.start()