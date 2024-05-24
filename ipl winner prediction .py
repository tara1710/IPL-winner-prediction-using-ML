#!/usr/bin/env python
# coding: utf-8

# In[3]:


#loading libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# In[9]:


#loading content
ipl=pd.read_csv("C:/Users/Tara/OneDrive/Desktop/matches.csv")
ipl


# In[10]:


ipl.head()


# In[11]:


#check records and columns
ipl.shape


# In[12]:


#frequency of player of match
ipl["player_of_match"].value_counts()


# In[13]:


#checking for top 10
ipl["player_of_match"].value_counts()[0:10]


# In[18]:


plt.figure(figsize=(9,5))
plt.bar(list(ipl["player_of_match"].value_counts()[0:10].keys()),
        list(ipl["player_of_match"].value_counts()[0:10]),color="red")


# In[19]:


ipl["result"].value_counts()


# In[20]:


ipl["toss_winner"].value_counts()


# In[24]:


plt.bar(list(ipl["toss_winner"].value_counts()[0:10].keys()),
        list(ipl["toss_winner"].value_counts()[0:10]))


# In[27]:


#team won batting first
batting=ipl[ipl["win_by_runs"]!=0]
batting


# In[28]:


batting.head()


# In[29]:


plt.figure(figsize=(10,5))
plt.hist(batting["win_by_runs"])
plt.title("Runs")


# In[30]:


batting["winner"].value_counts()


# In[31]:


plt.bar(list(batting['winner'].value_counts()[0:3].keys()),list(batting['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])


# In[33]:


plt.pie(list(batting['winner'].value_counts()),labels=list(batting['winner'].value_counts().keys()),autopct="%0.1f%%")


# In[35]:


batting_second=ipl[ipl["win_by_wickets"]!=0]
batting_second


# In[37]:


plt.hist(batting_second["win_by_wickets"],bins=30)


# In[38]:


batting_second["winner"].value_counts()


# In[39]:


plt.bar(list(batting_second["winner"].value_counts()[0:3].keys()),list(batting_second["winner"].value_counts()[0:3]),color=['purple','blue','red'])


# In[40]:


plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct="%0.1f%%")


# In[ ]:




