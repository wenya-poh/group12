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



textfile = open("lyrics/000~Jerry-Harrison~No-More-Reruns.txt")
raw_lines = []
lyric_words = {}

for i in textfile:
    raw_lines.append(i.split())

for line in raw_words:
    if line != []:


## Notes
# .splitlines() to get each line in a nested list