#!/usr/bin/env python
# coding: utf-8

# Lucas Invernizzi Day 7 Assignment

# 1)

# In[143]:


def divisible():
    out = []
    for i in range(1500,2701):
        if i % 7 == 0 and i % 5 == 0:
            out += [i]
    return out


# In[144]:


print(divisible())


# 2)

# In[145]:


def convertTemp(t):
    if t[-1] == 'C':
        temp = int((int(t[:-2]) * (9 / 5)) + 32)
        print('{} is {} in Fahrenheit'.format(t, str(temp)))
        return str(temp) + t[-2:-1] + 'C'
    elif t[-1] == 'F':
        temp = int((int(t[:-2]) - 32) * (5 / 9))
        print('{} is {} in Celcius'.format(t, str(temp)))
        return str(temp) + t[-2:-1] + 'F'
    else:
        print('This is not an accepted temperature unit.')


# In[146]:


convertTemp('60°C')


# In[147]:


convertTemp('45°F')


# 3)

# In[148]:


import random
def guessNum():
    genNum = random.randint(1,9)
    userNum = int(input('Guess a number between 1 and 9: '))
    while userNum != genNum:
        userNum = int(input('Wrong number! Guess again: '))
    print('Well guessed!')
        


# In[149]:


guessNum()


# 4)

# In[150]:


def asterisks():
    for i in range(1,3):
        for j in range(1,6):
            out = '* '
            if i == 1:
                print(out * j)
            else:
                if 5 - j != 0:
                    print(out * (5 - j))


# In[151]:


asterisks()


# 6)

# In[152]:


def revWord():
    word = input('Enter a word to be reversed: ')
    return word[::-1]


# In[153]:


revWord()


# 7)

# In[154]:


def numEvenOdd(data):
    numEven = 0
    numOdd = 0
    for i in data:
        if i % 2 == 0:
            numEven += 1
        else:
            numOdd += 1
    print('Number of even numbers: {}'.format(numEven))
    print('Number of odd numbers: {}'.format(numOdd))


# In[155]:


numEvenOdd([1,2,3,4,5,6,7,8,9])


# 8)

# In[156]:


def printValType(data):
    for i, val in zip(range(len(data)), data):
        print('Item {} is {} and has the type of {}'.format(i + 1, val, type(val)))


# In[157]:


printValType([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])


# 9)

# In[158]:


def printNums():
    for i in range(7):
        if i not in [3,6]:
            print(str(i) + ' ', end = '')
        else:
            continue


# In[159]:


printNums()

