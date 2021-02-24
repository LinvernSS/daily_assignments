#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 2 Assignment

# 1)

# In[126]:


a = 50 + 50


# In[127]:


print(a)


# In[128]:


b = 100 - 10


# In[129]:


print(b)


# 2)

# In[130]:


30+*6


# In[131]:


6^6


# In[132]:


6**6


# In[133]:


6+6+6+6+6+6


# 3)

# In[134]:


print("Hello World")


# In[135]:


print("Hello World : 10")


# 4)

# In[136]:


in_data = {'P' : 800000, 'R' : 6, 'L' : 103}


# In[137]:


in_data['R'] /= 1200


# In[138]:


d_num = in_data['R'] * ((1 + in_data['R']) ** in_data['L'])


# In[139]:


d_den = (((1 + in_data['R']) ** in_data['L']) - 1)


# In[140]:


M = -((in_data['P'] * d_num) // -d_den)


# In[141]:


print(M)

