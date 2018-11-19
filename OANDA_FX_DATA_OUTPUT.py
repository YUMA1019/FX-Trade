#!/usr/bin/env python
# coding: utf-8

# In[1]:


# OANDA API v20とPandasをインポート
from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import pandas as pd
import os
from os.path import join, dirname
from dotenv import load_dotenv
import sys
import key


# In[2]:


# OANDA API v20の口座IDとAPIトークン
accountID = key.aID
access_token = key.aTK


# In[3]:


# OANDAのデモ口座へのAPI接続
api = API(access_token=access_token, environment="practice")


# In[4]:


# APIに渡すパラメーターの設定
params = {
    "count":2000,
    "granularity":"S5"
}


# In[5]:


# APIへ過去為替レートをリクエスト
r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
api.request(r)


# In[6]:


# dataとしてPythonのリストへ過去レートを変換
data = []
for raw in r.response['candles']:
    data.append([raw['time'], raw['volume'], raw['mid']['o'], raw['mid']['h'], raw['mid']['l'], raw['mid']['c']])


# In[7]:


# リストからPandas DataFrameへ変換
df = pd.DataFrame(data)
df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
df = df.set_index('Time')
df.head()


# In[8]:


# date型を綺麗にする
df.index = pd.to_datetime(df.index)
df.tail()


# In[9]:


# データフレームからCSVファイルへ書き出し
df.to_csv('api-usdjpy-5s-0501.csv')


# In[ ]:




