#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys
import pprint
import pandas as pd

# fcoin APIを使用するためのモジュールパスを設定
sys.path.append("./fcoin-python-sdk")
sys.path.append("./common_python")
#print(sys.path)

from fcoin3 import Fcoin #if python3 use fcoin3 → from fcoin3 import Fcoin
from common import Common

#file_name = "../keys.csv"

common = Common()
#token = common.get_csv_val_by_key(file_name, "line_token")
common.set_line_token(os.environ["LINE_TOKEN"])


# In[55]:


fcoin = Fcoin()

data = pd.DataFrame(fcoin.get_market_ticker("btcusdt"))
latest_price = data.at["ticker","data"][0]
print(latest_price)
common.line_notify("BTC/USDT 最新価格： " + str(latest_price)) 

#print(fcoin.get_symbols())

#print(fcoin.get_currencies())

#fcoin.auth('you-key', 'you-secret') 

#print(fcoin.get_balance())

#print(fcoin.buy('fteth', 0.0001, 10))
#print(fcoin.sell('fteth', 0.002, 5))
#print(fcoin.cancel_order('6TfBZ-eORp4_2nO5ar6zhg0gLLvuWzTTmL1OzOy9OYg='))
#print(fcoin.get_candle('M1','fteth'))

