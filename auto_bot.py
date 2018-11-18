#!/usr/bin/env python
# coding: utf-8
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
# 長期保有の株や通貨に対して、売買タイミングを通知するボット
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

import os
import sys
import pprint
import pandas as pd

# 自作クラスを使用するためのモジュールパスを設定
sys.path.append("./fcoin-python-sdk")
sys.path.append("./common_python")
#print(sys.path)

# ---- Fcoin関連の情報取得用 ----
from fcoin3 import Fcoin #if python3 use fcoin3 → from fcoin3 import Fcoin
from common import Common

# ---- Bitbank関連の情報取得用 ----
import ccxt

# ---- 株価（Kabuクラス）関連の情報取得用 ----
from kabu import Kabu

# ---- LINEの自動通知用初期設定 ----
common = Common()
#common.set_line("9Cbs15MIrtk5phaHO9SzrrFQQ0XS85BiPmuWpWakibu")
common.set_line(os.environ["LINE_TOKEN"])

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
# データ取得＆通知のメインプログラム
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

# 情報を取得する先の設定
USE_FCOIN = False
TICKER_FCOIN = 'btcusdt'
UL_FCOIN = 10000
LL_FCOIN = 3000

USE_BITBANK = True
TICKER_BITBANK = 'XRP/JPY'
UL_BITBANK = 100
LL_BITBANK = 10

USE_KABU = True
TICKER_KABU = '6503'
UL_KABU = 2000
LL_KABU = 500

# ---- Fcoinからのデータ取得＆通知 ----
if USE_FCOIN:
    fcoin = Fcoin()
    data = pd.DataFrame(fcoin.get_market_ticker(TICKER_FCOIN))
    latest_price = data.at["ticker","data"][0]
    print(TICKER_FCOIN + ":" + str(latest_price))

    if latest_price > UL_FCOIN:
        text = "【FCOIN】"
        text += TICKER_FCOIN + ":" + str(latest_price) + " が "
        text += str(UL_FCOIN) + " を超えました！売りタイミングです！" + '\n'
        text += "（　＾ω＾）"
        common.send_message(text)
    elif latest_price < LL_FCOIN:
        text = "【FCOIN】"
        text += TICKER_FCOIN + ":" + str(latest_price) + " が "
        text += str(UL_FCOIN) + " を下回りました…損切タイミングです…" + '\n'
        common.send_message(text)

# ---- Bitbankからのデータ取得＆通知 ----
if USE_BITBANK:
    bitbank = ccxt.bitbank()
    data = bitbank.fetch_ticker(symbol=TICKER_BITBANK)
    latest_price = data['last']
    print(TICKER_BITBANK + ":" + str(latest_price))

    if latest_price > UL_BITBANK:
        text = "【BITBANK】"
        text += TICKER_BITBANK + ":" + str(latest_price) + " が "
        text += str(UL_BITBANK) + " を超えました！売りタイミングです！" + '\n'
        text += "（　＾ω＾）"
        common.send_message(text)
    elif latest_price < LL_BITBANK:
        text = "【BITBANK】"
        text += TICKER_BITBANK + ":" + str(latest_price) + " が "
        text += str(LL_BITBANK) + " を下回りました…損切タイミングです…" + '\n'
        common.send_message(text)

# ---- 株価関連からのデータ取得＆通知 ----
if USE_KABU:
    kabu = Kabu()
    df = kabu.get_last_by_stooq(TICKER_KABU)
    latest_price = int(df['Close'][:1])
    print(TICKER_KABU + ":" + str(latest_price))
    
    if latest_price > UL_KABU:
        text = "【KABU】"
        text += TICKER_KABU + ":" + str(latest_price) + " が "
        text += str(UL_KABU) + " を超えました！売りタイミングです！" + '\n'
        text += "（　＾ω＾）"
        common.send_message(text)
    elif latest_price < LL_KABU:
        text = "【KABU】"
        text += TICKER_FCOIN + ":" + str(latest_price) + " が "
        text += str(LL_KABU) + " を下回りました…損切タイミングです…" + '\n'
        common.send_message(text)