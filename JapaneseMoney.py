#!/usr/bin/env python
# coding: utf-8

# In[42]:


import requests
import pandas as pd
def line():
    url = 'https://notify-api.line.me/api/notify'
    token = 'x0fMifEC1uziaaoAdIxd3Cs9xl1Qw1PKG0OLWeRAURz'
    headers = {
        'Authorization': 'Bearer ' + token    # 設定權杖
    }
    data = {
        'message': 
        "\n"+
        f'日元已升值至{x}元'
    }
    data = requests.post(url, headers=headers, data=data)
url = 'https://www.bestxrate.com/bankrate/twsinopac.html'
resp = requests.get(url)
df = pd.read_html(resp.text)
x = float(df[0]['即期買入'][1])
if x >= 0.24 :
    line()

