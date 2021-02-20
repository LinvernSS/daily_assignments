#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 4 Assignment

# 1)

# In[2]:


l = [3, 'Word', 4.56]
print(l)


# 2)
# 
# To grab the 2 from the list you would call l[2][1].

# 3)
# 
# It would return ['b', 'c']

# 4)

# In[9]:


d = {'Monday' : 0,
     'Tuesday' : 1,
     'Wednesday' : 2,
     'Thursday' : 3,
     'Friday' : 4,
     'Saturday' : 5,
     'Sunday' : 6}


# 5)
# 
# It would throw an error since there are no quotation marks around the k1. If there were quotation marks it would return 2.

# Numbers divisible by 7 but not 5

# In[8]:


def findNum():
    out = ''
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            out += str(i) + ','
    print(out)


# In[9]:


findNum()


# Factorial
# I could have done this recursively like in the solution but I wanted to do something different since that answer is already provided for me.

# In[1]:


def factorial(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out


# In[2]:


print(factorial(8))


# Make Dictionary

# In[5]:


def makeDict(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i*i
    return d


# In[7]:


print(makeDict(8))

