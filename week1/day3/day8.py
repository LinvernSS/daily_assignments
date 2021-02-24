#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 8 Assignment

# 1)

# In[1]:


def func():
    print('Hello World')


# In[2]:


func()


# 2)

# In[3]:


def func1(name):
    print('Hi My name is {}'.format(name))


# In[4]:


func1('Google')


# 3)

# In[5]:


def func3(x,y,z):
    if z:
        return x
    else:
        return y


# In[6]:


print(func3('hello', 'goodbye', False))


# 4)

# In[7]:


def func4(x,y):
    return x * y


# In[8]:


func4(8, 7)


# 5)

# In[9]:


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# In[10]:


is_even(18)


# 6)

# In[11]:


def greaterThan(x,y):
    if x > y:
        return True
    else:
        return False


# In[12]:


greaterThan(1,2)


# 7)

# In[14]:


def sumArgs(*args):
    out = 0
    for i in args:
        out += i
    return out


# In[15]:


sumArgs(1,2,3,4,5,6,7,8)


# 8)

# In[16]:


def evenNums(*args):
    out = []
    for i in args:
        if i % 2 == 0:
            out += [i]
    return out


# In[17]:


evenNums(1,2,3,4,5,6,7,8)


# 9)

# In[20]:


def evenOddCase(word):
    out = ''
    for i, char in zip(range(len(word)), word):
        if i % 2 == 0:
            out += char.upper()
        else:
            out += char.lower()
    return out


# In[21]:


evenOddCase('Lucas Invernizzi')


# 10)

# In[22]:


def lesserNums(x,y):
    if x % 2 == 0 and y % 2 == 0:
        if x > y:
            return y
        else:
            return x
    else:
        if x > y:
            return x
        else:
            return y


# In[23]:


lesserNums(2,4)


# In[24]:


lesserNums(5,8)


# 11)

# In[33]:


def sameStart(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if word1[0] == word2[0]:
        return True
    else:
        return False


# In[36]:


sameStart('Hello', 'hi')


# In[37]:


sameStart('Hello', 'goodbye')


# 12)

# In[43]:


def twiceSeven(n):
    if n == 7:
        return 7
    elif n > 7:
        return 7 - ((n - 7) * 2)
    else:
        return 7 + ((7 - n) * 2)


# In[44]:


twiceSeven(9)


# In[45]:


twiceSeven(4)


# 13)

# In[53]:


def capFirstFourth(data):
    data = data.split(' ')
    out = ''
    for i, word in zip(range(len(data)), data):
        for j, char in zip(range(len(word)), word):
            if j in [0,3]:
                word = word[:j] + char.upper() + word[j+1:]
        data[i] = word
        
    for word in data:
        if word != data[-1]:
            out += word + ' '
        else:
            out += word
    return out


# In[55]:


capFirstFourth('lucas invernizzi')


# In[56]:


capFirstFourth('A function that capitalizes first and fourth character of a word in a string.')

