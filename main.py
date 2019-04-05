#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:35:30 2019

@author: wenya, darren
"""

#1 Make list of all lyric text titles
import os, sys

## Change working directory to the folder CONTAINING "lyrics" here - gives list of names of each file
path = "lyrics"
dirs = os.listdir(path)
file_titles = [] # list of file titles without .txt
file_txt_names = [] #list of tile titles with .txt

for file in dirs:
    file_txt_names.append(file)
file_txt_names.sort()

for file in dirs:
   file_titles.append(file)

for i in range(len(file_titles)):
    file_titles[i] = file_titles[i].replace(".txt","")
    





#3 Create the main lyric dictionary with id: [list of song words]
def read_song(txt_name):
    # returns all words for 1 song
    textfile = open(str(txt_name),encoding="utf8")
    raw_lines = []
    song_words = []
    
    for i in textfile:
        raw_lines.append(i.split())
    
    for line in raw_lines:
        if line != []:
            for word in line:
                song_words.append(word)
    return song_words

## Get List of all IDs, sorted from 000 to 10000 
def song_ID_list(titles):
    song_ID = []
    for i in titles:
        j = i.split('~')
        song_ID.append(j[0])
    return song_ID

song_ID_sorted = song_ID_list(file_titles)
song_ID_sorted.sort()
 
## Ensure that file_txt_names was mined from the fist set of code on top first. 
## Change working directory INTO the lyrics folder before running the next few lines
lyric_dict = {}
n=0
while n<=1000:
    lyric_dict[song_ID_sorted[n]] = read_song(file_txt_names[n])
    n+=1

#CODE FOR SONG LENGTH

#create list of song lengths to find max and min
song_length_list = []
n = 0
while n<=1000:
    song_length_list.append(len(lyric_dict[song_ID_sorted[n]]))
    n+=1
max_ = max(song_length_list)
min_ = min(song_length_list)

#create dictionary consisting id, song length
length_dict = {}

n = 0
while n<=1000:
    length_dict[song_ID_sorted[n]] = ((1-0)/(max_-min_)*(len(lyric_dict[song_ID_sorted[n]])-max_)+1)    
    n+=1
    


## Notes
# Lyric filenames go from 000 to 1000
# .splitlines() to get each line in a nested list
    
    
    
#5 ALWAYS RUN LAST! Create final output dictionary(extract id, artist, title) 
    
def extract_(titles):
    list_1 = []
    for i in titles:
        b = i.split('~')   
        dict_1 = {"id" : b[0], "artist" : b[1], "title" : b[2], 'kid_safe': 0, 'love': 0, 'mood': 0, 'length': length_dict[b[0]], 'complexity': 0}
        list_1.append(dict_1)
    return list_1
    
output_list = extract_(file_titles)

output_list[0] 