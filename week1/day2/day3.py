#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 3 Assignment

# 1)

# In[2]:


'Hello World'[8]


# 2)

# In[3]:


'thinker'[2:-2]


# The output of s[1] is 'e'

# 3)

# The output of s[2:] is 'mmy'

# 4)

# In[16]:


set(list('Mississippi'))


# You can't do it just by turning it into a set, it will throw an error. You need to make it a list before you cast it into a set.

# 5)

# In[23]:


in_data = '3\nStars\nO, a kak Uwakov lil vo kawu kakao!\nSome men interpret nine memos'


# In[50]:


import string
def isPalindrome(data):
    out = ''
    data = data.split('\n')
    for i in range(1, int(data[0])+1):
        temp = data[i]
        temp = temp.translate(str.maketrans('', '', string.punctuation))
        temp = temp.lower().replace(" ", "")
        if temp == temp[::-1]:
            out += 'Y '
        else:
            out += 'N '
    return out
    


# In[51]:


print(isPalindrome(in_data))

