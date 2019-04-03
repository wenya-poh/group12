#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:35:30 2019

@author: wenya, darren
"""

# Make list of all lyric text titles
import os, sys

# Change working directory to the folder CONTAINING "lyrics" here - gives list of names of each file
path = "lyrics"
dirs = os.listdir(path)
file_titles = []

for file in dirs:
   file_titles.append(file)
file_titles.sort()


def read_song(txt_name):
    textfile = open(str(txt_name))
    raw_lines = []
    song_words = []
    
    for i in textfile:
        raw_lines.append(i.split())
    
    for line in raw_words:
        if line != []:
            for word in line:
                song_words.append(word)
    return song_words

# Change working directory INTO the lyrics folder before running this
## List of all IDs   
song_ID = []
for i in file_titles:
    song_ID.append(i[0:3])
song_ID.sort()


lyric_dict = {}
n=0
file_titles.sort()
while n<=1001:
    lyric_dict[song_ID[n]] = read_song(file_titles[n])
    n+=1



for i in file_titles:
    song = read_song(i)
    
    
    

## Notes
# Lyric filenames go from 000 to 1000
# .splitlines() to get each line in a nested list