#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ライブラリーのインポート
import pandas as pd
import oandapyV20
import oandapyV20.endpoints.orders as orders
import sys
import key


# In[2]:


# OANDA API v20の口座IDとAPIトークン
accountID = key.aID
access_token = key.aTK


# In[3]:


# APIへ接続
api = oandapyV20.API(access_token=access_token)


# In[4]:


#成行注文
data = {
  "order": {
    "instrument": "USD_JPY",
    "units": "+10000",
    "type": "MARKET",
    "positionFill": "DEFAULT"
  }
}


# In[5]:


# API経由で成行注文を実行
r = orders.OrderCreate(accountID, data=data)
api.request(r)


# In[6]:


# ドル円が109.650で1万通貨売りの指値注文をAPI経由でやってみる
data = {
  "order": {
    "price" : "112.800",
    "instrument": "USD_JPY",
    "units": "-10000",
    "type": "LIMIT",
    "positionFill": "DEFAULT"
  }
}


# In[7]:


# 全てのペンディング注文を取得する
r = orders.OrdersPending(accountID)
api.request(r)


# In[8]:


# 注文をキャンセル
r = orders.OrderCancel(accountID=accountID, orderID=13)
api.request(r)


# In[ ]:





# In[ ]:




