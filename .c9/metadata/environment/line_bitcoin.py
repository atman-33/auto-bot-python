{"filter":false,"title":"line_bitcoin.py","tooltip":"/line_bitcoin.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":20},"action":"remove","lines":["from selenium import webdriver","browser = webdriver.PhantomJS()  # DO NOT FORGET to set path","browser.get(\"https://www.google.co.jp/\") # enables to access page","print(browser.title)"],"id":2},{"start":{"row":0,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["#!/usr/bin/env python","# coding: utf-8","","# In[2]:","","","import os","import sys","import pprint","import pandas as pd","","# fcoin APIを使用するためのモジュールパスを設定","sys.path.append(\"../fcoin-python-sdk\")","sys.path.append(\"../common_python\")","#print(sys.path)","","from fcoin3 import Fcoin #if python3 use fcoin3 → from fcoin3 import Fcoin","from common import Common","","file_name = \"../keys.csv\"","","common = Common()","token = common.get_csv_val_by_key(file_name, \"line_token\")","common.set_line_token(token)","","","# In[55]:","","","fcoin = Fcoin()","","data = pd.DataFrame(fcoin.get_market_ticker(\"btcusdt\"))","latest_price = data.at[\"ticker\",\"data\"][0]","print(latest_price)","common.line_notify(\"BTC/USDT 最新価格： \" + str(latest_price)) ","","#print(fcoin.get_symbols())","","#print(fcoin.get_currencies())","","#fcoin.auth('you-key', 'you-secret') ","","#print(fcoin.get_balance())","","#print(fcoin.buy('fteth', 0.0001, 10))","#print(fcoin.sell('fteth', 0.002, 5))","#print(fcoin.cancel_order('6TfBZ-eORp4_2nO5ar6zhg0gLLvuWzTTmL1OzOy9OYg='))","#print(fcoin.get_candle('M1','fteth'))","",""]}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"remove","lines":["."],"id":3},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"remove","lines":["."]}],[{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"insert","lines":["."],"id":4}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["."],"id":5}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["#"],"id":14}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["#"],"id":15}],[{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["\""],"id":16},{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["\""]}],[{"start":{"row":23,"column":24},"end":{"row":23,"column":29},"action":"remove","lines":["token"],"id":17}],[{"start":{"row":23,"column":23},"end":{"row":23,"column":24},"action":"insert","lines":["L"],"id":18},{"start":{"row":23,"column":24},"end":{"row":23,"column":25},"action":"insert","lines":["I"]},{"start":{"row":23,"column":25},"end":{"row":23,"column":26},"action":"insert","lines":["N"]},{"start":{"row":23,"column":26},"end":{"row":23,"column":27},"action":"insert","lines":["E"]},{"start":{"row":23,"column":27},"end":{"row":23,"column":28},"action":"insert","lines":["_"]},{"start":{"row":23,"column":28},"end":{"row":23,"column":29},"action":"insert","lines":["T"]},{"start":{"row":23,"column":29},"end":{"row":23,"column":30},"action":"insert","lines":["O"]},{"start":{"row":23,"column":30},"end":{"row":23,"column":31},"action":"insert","lines":["K"]}],[{"start":{"row":23,"column":31},"end":{"row":23,"column":32},"action":"insert","lines":["E"],"id":19},{"start":{"row":23,"column":32},"end":{"row":23,"column":33},"action":"insert","lines":["N"]}]]},"ace":{"folds":[],"scrolltop":102,"scrollleft":0,"selection":{"start":{"row":23,"column":4},"end":{"row":23,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1541516230486,"hash":"14d18f136ff3d77a7ea09350ae7e3b09dfec1c4d"}