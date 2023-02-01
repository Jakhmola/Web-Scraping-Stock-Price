import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime


def get_price(symbol):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
    url = f"https://uk.finance.yahoo.com/quote/{symbol}"
    web_content = requests.get(url, headers=header)
    soup = BeautifulSoup(web_content.text, 'html.parser')
    price_ = soup.find('fin-streamer', {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    # print(price.text)

    if price_ is None:
        price_ = 999999
    price_ = float(price_.replace(',', ''))
    return price_


stock_names = ['BTC-GBP', 'ETH-GBP', 'LTC-GBP', 'LINK-GBP']

for _ in range(1, 101):
    dt = datetime.datetime.now()
    dt = dt.strftime('%Y-%m-%d %H:%M:%S')
    price = []
    col = [dt]
    for stock in stock_names:
        price.append(get_price(stock))
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('real_time_stock_price.csv', mode='a', header=False)
    print(col)
