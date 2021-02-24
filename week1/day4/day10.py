#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 10 Assignment

# 1)

# In[16]:


def bmi(in_data):
    in_data = in_data.split('\n')
    out = ''
    for i in range(1, int(in_data[0]) + 1):
        person = in_data[i].split()
        weight = int(person[0])
        height = float(person[1])
        bmi = weight / (height ** 2)
        if bmi >= 30:
            out += 'obese '
        elif bmi >= 25:
            out += 'over '
        elif bmi >= 18.5:
            out += 'normal '
        else:
            out += 'under '
    return out.strip()


# In[17]:


data = '3\n80 1.73\n55 1.56\n49 1.91'


# In[18]:


bmi(data)

