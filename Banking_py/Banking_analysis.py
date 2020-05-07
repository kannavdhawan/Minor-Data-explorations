#!/usr/bin/env python
# coding: utf-8

# In[63]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly
import cufflinks as cf
cf.go_offline()


# ## Data
# Banks
# * Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo

# In[7]:


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)


# In[8]:


JPM = data.DataReader("JPM", 'yahoo', start, end)
MS = data.DataReader("MS", 'yahoo', start, end)
WFC = data.DataReader("WFC", 'yahoo', start, end)
BAC = data.DataReader("BAC", 'yahoo', start, end)
C = data.DataReader("C", 'yahoo', start, end)
GS = data.DataReader("GS", 'yahoo', start, end)


# In[9]:


JPM


# In[11]:


#panel object
# df = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],'yahoo', start, end)


# In[20]:


# df.head()


# ticker symbol list

# In[13]:


tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


# In[14]:


stocks=pd.concat([BAC, C, GS, JPM, MS, WFC],keys=tickers,axis=1)


# In[15]:


stocks.head()


# In[17]:


stocks.columns.names= ['Bank Ticker','Stock Details'] 


# In[18]:


stocks.head()


# In[21]:


stocks.xs(key='Close',axis=1,level='Stock Details')


# In[22]:


stocks.xs(key='Close',axis=1,level='Stock Details').max()


# In[23]:


returns=pd.DataFrame()


# In[24]:


for tick in tickers:
    returns[tick+' Return'] = stocks[tick]['Close'].pct_change()
returns.head()


# In[31]:


sns.pairplot(returns)


# In[38]:


for ticks in tickers:
    print(returns.loc[returns[ticks+' Return']==returns[ticks+' Return'].max()])


# In[40]:


returns.idxmin()


# In[41]:


returns.idxmax() #returns column wise max index


# In[42]:


returns.std()


# In[55]:


returns.reset_index()['Date'][0].year


# In[54]:


returns.loc['2015-01-01':'2015-12-31'].std()


# In[56]:


returns.head()


# In[60]:


sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'],color='blue',bins=80,rug=True)
#y axis can be seen for the relative comparison between the various categories 
#area  under the curve is 1


# In[61]:


sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'],color='blue',bins=80,rug=True)
#y axis can be seen for the relative comparison between the various categories 
#area  under the curve is 1


# In[64]:


sns.set_style('whitegrid')


# In[87]:


for ticks in tickers:
    stocks[ticks]['Close'].plot(label=ticks)
plt.legend()


# In[81]:


stocks_close=stocks.xs(key='Close',level='Stock Details',axis=1)


# In[83]:


stocks_close


# In[82]:


stocks_close.plot(figsize=(12,4))


# In[77]:


stocks.xs(key='Close',axis=1,level='Stock Details').iplot()


# In[ ]:


#MOving AVerage


# In[110]:


stocks['C']['Close'].loc['2009-01-01':'2010-01-01'].rolling(window=50).mean().plot(label='50 Day Avg')
stocks['C']['Close'].loc['2009-01-01':'2010-01-01'].plot(label='C CLOSE')
plt.legend()


# In[90]:


stocks_close.corr()


# In[92]:


sns.heatmap(stocks_close.corr(),annot=True)


# In[93]:


sns.clustermap(stocks_close.corr(),annot=True)


# In[96]:


stocks_close.corr().iplot(kind='heatmap')

