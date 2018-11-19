#!/usr/bin/env python
# coding: utf-8

# In[31]:


# coding: UTF-8
import os
import os.path
import dotenv
import sys
#dotenv_path = join(dirname(os.path.abspath(sys.argv[0])), '.env')
dotenv_path = str.join(os.path.dirname('__file__'), '.env')
dotenv.load_dotenv(dotenv_path)

# OANDA API v20の口座IDとAPIトークン
aID = os.environ.get("accountID")
aTK = os.environ.get("access_token")


# In[ ]:




