#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 9 Assignment

# 1)

# In[16]:


def bookAccount(account):
    priceAdjust = lambda x, y : ((x*y) + 10) if (x*y<100) else (x*y) 
    makeTuple = lambda a : (a[0], priceAdjust(a[2], a[3]))
    return list(map(makeTuple, account))


# In[17]:


data = [[34587, 'Learning Python, Mark Lutz', 4, 40.95], 
        [98762, 'Programming Python, Mark Lutz', 5, 56.80], 
        [77226, 'Head First Python, Paul Barry', 3, 32.95], 
        [88112, 'Einführung in Python3, Bernd Klein', 3, 24.99]]


# In[18]:


bookAccount(data)


# 2)

# In[98]:


def bookAccount1(account):
    getPrice = lambda b : b[1] * b[2]
    priceWrap = lambda a : sum(list(map(getPrice, a)))
    priceAdjust = lambda p : priceWrap(p) if priceWrap(p) < 100 else priceWrap(p) + 10
    makeTuple = lambda o : (o[0], priceAdjust(o[1:]))
    return list(map(makeTuple, account))


# In[99]:


data = [[34587, ('Learning Python, Mark Lutz', 4, 40.95), ('Programming Python, Mark Lutz', 5, 56.80)],  
        [77226, ('Head First Python, Paul Barry', 3, 32.95), ('Einführung in Python3, Bernd Klein', 3, 24.99)]]


# In[100]:


bookAccount1(data)

