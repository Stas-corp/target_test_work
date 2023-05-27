import ccxt
import pandas as pd

exchange = ccxt.binance()
symbol = 'ETH/USDT'
timeframe = '4h'
period = exchange.milliseconds() - 90 * 24 * 60 * 60 * 1000  # 90 дней в миллисекундах

# Получаем исторические данные по ценам
history_eth_usdt = exchange.fetch_ohlcv(symbol, timeframe, since=period, limit=40000)
print(history_eth_usdt)
# Преобразуем данные в DataFrame
df = pd.DataFrame(history_eth_usdt, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Приводим столбец timestamp к формату даты
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Устанавливаем столбец timestamp как индекс
df.set_index('timestamp', inplace=True)

print(df)

df.to_csv('example.csv')