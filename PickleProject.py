#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import datetime


# In[2]:


MyFile = "pickle.pik"


# In[3]:


a = ["Ali Naqvi", "John Doe", "Jim Schaffer"]


# In[4]:


b = ["1234 Ali’s lane", "345 John’s address", "No known address"]


# In[5]:


c = float(34.25)


# In[6]:


d = datetime.date.today()


# In[7]:


def pickleDump(names, address, temp, date, file):
    with open(file, 'wb') as f:
        pickle.dump(names, f)
        pickle.dump(address, f)
        pickle.dump(temp, f)
        pickle.dump(date, f)


# In[8]:


def pickleLoad(file):
    with open(file, 'r') as f:
        MyLine = f.readline()
    print(MyLine)


# In[9]:


pickleDump(a, b, c, d, MyFile)


# In[10]:


MyOutput = pickleLoad(MyFile)

