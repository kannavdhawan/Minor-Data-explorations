#!/usr/bin/env python
# coding: utf-8

# ### -------------------------------------------------911 Calls Capstone Project---------------------------------------------------------------------

# #### -----------------------------------------------------------------------------columns---------------------------------------------------------------------------------------------------
# 1. lat : Latitude(String variable)
# 2. lng: Longitude(String variable)
# 3. desc: Description of the Emergency Call(String variable)
# 4. zip: Zipcode(String variable)
# 5. title: Title(String variable)
# 6. timeStamp: Format YYYY-MM-DD HH:MM:SS(String variable)
# 7. twp: Township(String variable)
# 8. addr: Address(String variable)
# 9. e: Dummy variable(String variable)

# ____
# Imports

# In[1]:


import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# Reading the csv file as a dataframe 'df'

# In[3]:


df=pd.read_csv('911.csv')


# In[4]:


df.info()


# In[5]:


df.head()


# Finding top 5 zipcodes for 911 calls

# In[6]:


df['zip'].value_counts().head()


# Finding top 5 twp's for 911 calls

# In[7]:


df['twp'].value_counts().head()


# finding unique values

# In[8]:


df['title'].nunique()


# In[9]:


df['zip'].nunique()


# In[10]:


df['twp'].nunique()


# ### Creating new features out of existing ones

# In[11]:


df['Reason']=df['title'].apply(lambda x: x.split(':')[0])


# In[12]:


df.head()


# #### Reason and number of calls

# In[13]:


df['Reason'].value_counts()


# ####  Plot

# In[14]:


sns.countplot(x='Reason',data=df,palette='coolwarm')


# ___
# Timestamp Datatype

# In[15]:


type(df['timeStamp'][0])


# convedrsion into datetime

# In[16]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])
type(df['timeStamp'][0])


# In[17]:


df.head()


# In[18]:


time=df['timeStamp'].iloc[0]
time.hour


# In[19]:


time


# In[20]:


df['Hour']=df['timeStamp'].apply(lambda x: x.hour)
df['Month']=df['timeStamp'].apply(lambda x: x.month)
df['Day']=df['timeStamp'].apply(lambda x: x.dayofweek)


# In[21]:


df.head()


# mapping into days of week

# In[22]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[23]:


df['Day']=df['Day'].map(dmap)


# In[24]:


df.head()


# countplot for Day as category with distribution(hue) as reason

# In[25]:


sns.countplot(x='Day',data=df,hue='Reason',palette='magma')
plt.legend(loc='best',bbox_to_anchor=(1,0.5))


# **Now doing the same for Month:**

# In[26]:


sns.countplot(x='Month',data=df,hue='Reason',palette='dark')
plt.legend(loc='best',bbox_to_anchor=(1,0.5))


# **Groupby object with count as aggregate function**

# In[27]:


df1=df.groupby('Month').count()


# In[28]:


df1


# In[29]:


plt.plot(df1['twp'])


# In[30]:


sns.set_style('whitegrid')
sns.lmplot(x="Month",y="twp",data=df1.reset_index())


# Date column form timestamp

# In[31]:


df['timeStamp'][0].date()


# In[32]:


df['Date']=df['timeStamp'].apply(lambda x:x.date())


# In[33]:


df.head()


# ** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

# In[34]:


df2=df.groupby('Date').count()


# In[35]:


df2.head()


# In[36]:


sns.lineplot(x="Date",y="Reason",data=df2.reset_index())


# In[37]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')


# In[38]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')


# In[39]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('FIRE')


# **Heatmaps and clustermaps**

# In[40]:


heat_df=df.groupby(by=['Day','Hour']).count()['Reason'].unstack()
heat_df


# In[41]:


plt.figure(figsize=(12,6))
sns.heatmap(heat_df,cmap='magma',linewidth=2)


# creating clustermap using this same DataFrame.

# In[42]:


plt.figure(figsize=(12,6))
sns.clustermap(heat_df,cmap='magma',linewidth=2)


# Now repeating for a DataFrame that shows the Month as the column.

# In[43]:


heat_df_month=df.groupby(by=['Day','Month']).count()['Reason'].unstack()
heat_df_month.head()


# In[44]:


plt.figure(figsize=(10,8))
sns.heatmap(heat_df_month,cmap='coolwarm',linewidth=2,linecolor='black')


# In[45]:


plt.figure(figsize=(10,8))
sns.clustermap(heat_df_month,cmap='coolwarm',linewidth=2,linecolor='black')

