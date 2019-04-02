#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:35:30 2019

@author: wenya, darren
"""

# Make list of all lyric text titles
import os, sys

path = "lyrics"
dirs = os.listdir( path )
file_titles = []

for file in dirs:
   file_titles.append(file)

for i in range(len(file_titles)):
    file_titles[i] = file_titles[i].replace(".txt","")
    

#extract id, artist, title
list_1 = []
    
def extract_(x):
    
    import re
    for i in range(1000):
        b = re.split('~' ,x[i])   
        dict_1 = {"id" : b[0], "artist" : b[1], "title" : b[2], 'kid_safe': 0, 'love': 0, 'mood': 0, 'length': 0, 'complexity': 0}
        list_1.append(dict_1)
    return list_1
    
extract_(file_titles)


textfile = open("lyrics/000~Jerry-Harrison~No-More-Reruns.txt")
raw_lines = []
lyric_words = {}

for i in textfile:
    raw_lines.append(i.split())

for line in raw_words:
    if line != []:


## Notes
# .splitlines() to get each line in a nested list