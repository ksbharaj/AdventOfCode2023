#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
import re
import pandas as pd
import tqdm


# In[2]:


curr_loc = os.getcwd()


# In[3]:


with open(curr_loc+'/Task_3/input.txt', 'r') as file:
    content = file.read()

# Split each line into a list of characters
lines = content.split('\n')


# In[4]:


lines.pop(-1)


# # Part 1

# In[17]:


y_len = len(lines)
x_len = len(lines[0])


# In[18]:


directions = np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])


# In[19]:


split_characters = [[char for char in line] for line in lines]


# In[20]:


def symbol_seeker(grid, x, y):
    answer = False
    for i in range((y_len)):
        for j in range(x_len):
            locas = [x,y] + directions
            for loca in locas:
                if loca[0] >= 0 and loca[0]<y_len:
                    if loca[1] >= 0 and loca[1]<x_len:
                        if grid[loca[0]][loca[1]] != '.' and not grid[loca[0]][loca[1]].isdigit():
                            answer = True
                            return answer


# In[21]:


tracker = []
mapped = []
total = 0
for i in tqdm.tqdm(range((y_len))):
    for j in range(x_len):
        if [i,j] not in mapped:
            if split_characters[i][j] != '.' and split_characters[i][j].isdigit():
                try:
                    next_char = split_characters[i][j+1]
                    next_to_next_char = split_characters[i][j+2]
                    if next_char.isdigit() and next_to_next_char.isdigit():
                        if symbol_seeker(split_characters, i, j) or symbol_seeker(split_characters, i, j+1) or symbol_seeker(split_characters, i, j+2):
                            # print(split_characters[i][j], split_characters[i][j+1], split_characters[i][j+2])
                            # print('found a symbol')
                            total += int(split_characters[i][j]+ split_characters[i][j+1]+ split_characters[i][j+2])
                            mapped.append([i,j])
                            mapped.append([i,j+1])
                            mapped.append([i,j+2])
                    elif next_char.isdigit() and not next_to_next_char.isdigit():
                        if symbol_seeker(split_characters, i, j) or symbol_seeker(split_characters, i, j+1):
                            # print(split_characters[i][j], split_characters[i][j+1])
                            # print('found a symbol')
                            total += int(split_characters[i][j]+ split_characters[i][j+1])
                            mapped.append([i,j])
                            mapped.append([i,j+1])
                    else:
                        if symbol_seeker(split_characters, i, j):
                            # print(split_characters[i][j])
                            # print('found a symbol')
                            total += int(split_characters[i][j])
                            mapped.append([i,j])    
                except:
                    pass
            else:
                pass


# In[22]:


total


# # Part 2

# In[5]:


y_len = len(lines)
x_len = len(lines[0])


# In[6]:


directions = np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])


# In[7]:


split_characters = [[char for char in line] for line in lines]


# In[8]:


def symbol_seeker(grid, x, y):
    answer = False
    for i in range((y_len)):
        for j in range(x_len):
            locas = [x,y] + directions
            for loca in locas:
                if loca[0] >= 0 and loca[0]<y_len:
                    if loca[1] >= 0 and loca[1]<x_len:
                        if grid[loca[0]][loca[1]] != '.' and not grid[loca[0]][loca[1]].isdigit():
                            if grid[loca[0]][loca[1]] == '*':
                                answer = True
                                return answer, [loca[0], loca[1]]
                            # answer = True
                            # return answer


# In[9]:


tracker = []
mapped = []
symbol_loc = {} ## Put where the key is the [x,y] location and vlaue is the number
total = 0
for i in tqdm.tqdm(range((y_len))):
    for j in range(x_len):
        if [i,j] not in mapped:
            if split_characters[i][j] != '.' and split_characters[i][j].isdigit():
                try:
                    next_char = split_characters[i][j+1]
                    next_to_next_char = split_characters[i][j+2]
                    if next_char.isdigit() and next_to_next_char.isdigit():
                        if symbol_seeker(split_characters, i, j) or symbol_seeker(split_characters, i, j+1) or symbol_seeker(split_characters, i, j+2):
                            val_1 = symbol_seeker(split_characters, i, j)
                            val_2 = symbol_seeker(split_characters, i, j+1)
                            val_3 = symbol_seeker(split_characters, i, j+2)
                            to_be_added = []
                            if val_1 != None:
                                if val_1[1] not in to_be_added:
                                    to_be_added.append(val_1[1])
                            if val_2 != None:
                                if val_2[1] not in to_be_added:
                                    to_be_added.append(val_2[1])
                            if val_3 != None:
                                if val_3[1] not in to_be_added:
                                    to_be_added.append(val_3[1])
                            for loca in to_be_added:
                                if tuple(loca) in symbol_loc.keys():
                                    # print(int(split_characters[i][j]+ split_characters[i][j+1]+ split_characters[i][j+2]))
                                    # print("JACKPOT")
                                    sum_1 = int(split_characters[i][j]+ split_characters[i][j+1]+ split_characters[i][j+2])
                                    sum_2 = symbol_loc[tuple(loca)]
                                    total += sum_1*sum_2
                                else:
                                    symbol_loc[tuple(loca)] = int(split_characters[i][j]+ split_characters[i][j+1]+ split_characters[i][j+2])
                            mapped.append([i,j])
                            mapped.append([i,j+1])
                            mapped.append([i,j+2])
                                    
                    elif next_char.isdigit() and not next_to_next_char.isdigit():
                        if symbol_seeker(split_characters, i, j) or symbol_seeker(split_characters, i, j+1):
                            val_1 = symbol_seeker(split_characters, i, j)
                            val_2 = symbol_seeker(split_characters, i, j+1)
                            to_be_added = []
                            if val_1 != None:
                                if val_1[1] not in to_be_added:
                                    to_be_added.append(val_1[1])
                            if val_2 != None:
                                if val_2[1] not in to_be_added:
                                    to_be_added.append(val_2[1])
                            for loca in to_be_added:
                                if tuple(loca) in symbol_loc.keys():
                                    # print(int(split_characters[i][j]+ split_characters[i][j+1]))
                                    # print("JACKPOT")
                                    sum_1 = int(split_characters[i][j]+ split_characters[i][j+1])
                                    sum_2 = symbol_loc[tuple(loca)]
                                    total += sum_1*sum_2
                                    mapped.append([i,j])
                                    mapped.append([i,j+1])
                                else:
                                    symbol_loc[tuple(loca)] = int(split_characters[i][j]+ split_characters[i][j+1])
                            mapped.append([i,j])
                            mapped.append([i,j+1])
                    else:
                        if symbol_seeker(split_characters, i, j):
                            val_1 = symbol_seeker(split_characters, i, j)
                            to_be_added = []
                            if val_1 != None:
                                if val_1[1] not in to_be_added:
                                    to_be_added.append(val_1[1])
                            for loca in to_be_added:
                                if tuple(loca) in symbol_loc.keys():
                                    # print(int(split_characters[i][j]+ split_characters[i][j+1]))
                                    # print("JACKPOT")
                                    sum_1 = int(split_characters[i][j]+ split_characters[i][j+1])
                                    sum_2 = symbol_loc[tuple(loca)]
                                    total += sum_1*sum_2
                                    mapped.append([i,j])
                                    mapped.append([i,j+1])
                                else:
                                    symbol_loc[tuple(loca)] = int(split_characters[i][j]+ split_characters[i][j+1])
                            mapped.append([i,j])

                except:
                    pass
            else:
                pass


# In[10]:


total


# In[199]:


lines


# In[ ]:





# In[135]:


int(split_characters[i][j]+ split_characters[i][j+1]+ split_characters[i][j+2])


# In[ ]:





# In[129]:


lines


# In[ ]:





# In[99]:


set([symbol_seeker(split_characters, i, j), symbol_seeker(split_characters, i, j+1), symbol_seeker(split_characters, i, j+2)])


# In[90]:


values = set([split_characters[i][j], split_characters[i][j+1], split_characters[i][j+2]])
if len(values) == 1:
    print("The value is:", values.pop())
else:
    print("No unique value found.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:


def number_seeker(grid, x, y):
    answer = False
    for i in range((y_len)):
        for j in range(x_len):
            locas = [x,y] + directions
            for loca in locas:
                if loca[0] >= 0 and loca[0]<y_len:
                    if loca[1] >= 0 and loca[1]<x_len:
                        if grid[loca[0]][loca[1]] != '.' and grid[loca[0]][loca[1]].isdigit():
                            answer = True
                            return answer, grid[loca[0]][loca[1]]


# In[40]:


tracker = []
mapped = []
total = 0
for i in tqdm.tqdm(range((y_len))):
    for j in range(x_len):
        if split_characters[i][j] != '.' and not split_characters[i][j].isdigit():
            if split_characters[i][j] == '*':
                print(split_characters[i][j])
                print(number_seeker(split_characters, i, j))


# In[41]:


lines


# In[ ]:




