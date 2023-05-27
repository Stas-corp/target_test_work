import ccxt
import pandas as pd
import statsmodels.api as sm

exchange = ccxt.binance()

def get_history_tiket(symbol: str, limit=500, timeframe='1d') -> pd.DataFrame:
    end_time = exchange.milliseconds()
    start_time = end_time - limit * 24 * 60 * 60 * 1000
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, start_time, limit)
    df = pd.DataFrame(ohlcv, columns=['time', f'open', 'high', 'low', 'close', 'volume'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df.set_index('time', inplace=True)
    return df

# данные для пары валют ETH/USDT
ETH_df = get_history_tiket('ETH/USDT')

# данные для пары валют BTC/USDT
BTC_df = get_history_tiket('BTC/USDT')

df = pd.concat([ETH_df, BTC_df['close'].rename('close_x')], axis=1)
df.dropna(inplace=True)
df.to_csv('t2.csv')

X = sm.add_constant(df['close_x'])
model = sm.OLS(df['close'], X).fit()
print(model.summary())