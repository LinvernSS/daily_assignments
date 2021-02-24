#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 6 Assignment

# Three is a Crowd

# In[30]:


l = ['Michael', 'Emily', 'John', 'Mary']


# In[31]:


def isCrowd(names):
    if len(names) > 3:
        print('The room is crowded!')


# In[32]:


isCrowd(l)


# In[33]:


l.pop()
l.pop()
print(l)


# In[34]:


isCrowd(l)


# Three is a Crowd part 2

# In[35]:


def isCrowd(names):
    if len(names) > 3:
        print('The room is crowded!')
    else:
        print('The room is not very crowded!')


# In[36]:


isCrowd(l)


# Six is a Mob

# In[45]:


l = ['Michael', 'Emily', 'John', 'Mary', 'Robert', 'Jessica']


# In[38]:


def isCrowd(names):
    if len(names) > 5:
        print('There is a mob in the room!')
    elif len(names) > 2:
        print('The room is crowded!')
    elif len(names) > 0:
        print('The room is not very crowded!')
    else:
        print('The room is empty.')


# In[46]:


isCrowd(l)
l.pop()
isCrowd(l)
l.pop()
isCrowd(l)
l.pop()
isCrowd(l)
l.pop()
isCrowd(l)
l.pop()
isCrowd(l)
l.pop()
isCrowd(l)

