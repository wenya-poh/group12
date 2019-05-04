#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:35:23 2019

@author: wenya
"""

# HELPER FUNCTIONS
# Function that returns the individual words for the text file input
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
                song_words.append(word.lower())
    return song_words


## Get List of all IDs, sorted from 000 to 10000 
def song_ID_list(titles):
    song_ID = []
    for i in titles:
        j = i.split('~')
        song_ID.append(j[0])
    return song_ID


## Function to return a list of songs with each line as a string
def read_song_lines(txt_name):
    # returns the first line of each song
    textfile = open(str(txt_name),encoding="utf8")
    raw_lines = []
    for i in textfile:
        raw_lines.append(i.strip('\n').rstrip().lower())
    return raw_lines


def original_dict(file_path):   
    import os, sys
    #1 Read files in folder. To enter the path of the folder containing the txt files
    path = str(file_path)
    
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
    
    #2 Create the main lyric dictionary with individual words. format is id: [list of song words]
    song_ID_sorted = song_ID_list(file_titles)
    song_ID_sorted.sort()
    lyric_dict = {}
    n=0
    while n<=1000:
        lyric_dict[song_ID_sorted[n]] = read_song(path+'/'+file_txt_names[n])
        n+=1
    
    #3 Create the main line dictionary with sentences. format is id: [list of lyric sentences]
    lines_dict = {}
    n=0
    while n<=1000:
        lines_dict[song_ID_sorted[n]] = read_song_lines(path+'/'+file_txt_names[n])
        n+=1
    
    return (lyric_dict, lines_dict)

lyric_dict = original_dict('Lyrics')[0]
lines_dict = original_dict('Lyrics')[1]




def translate_strings(song_words_):
    from textblob import TextBlob
    #Input: output from song_words, a list of words from a song, e.g. ['what','a','great','day']
    translated = []
    for word in song_words_:
        if len(word) >= 3:
            w = TextBlob(word).translate(to='en')
            translated.append(str(w))
    return translated

import googletrans
from googletrans import Translator
## translate_list iterates over a list of strings and translates 
def translate_google(song_words_):
     translator = Translator()
     translated = []
     for i in song_words_:
         t = translator.translate(i,dest='en')
         translated.append(t.text)
     return translated

non_eng_dict = {'016': 'es', '023': 'pt', '026': 'de', '032': 'pt', '051': 'es', '074': 'zu', '082': 'fr', '093': 'es', '106': 'es', '111': 'es', '146': 'pt', '152': 'es', '154': 'it', '155': 'es', '157': 'pt', '170': 'fr', '177': 'es', '191': 'es', '194': 'es', '215': 'es', '226': 'es', '232': 'fr', '248': 'es', '252': 'fr', '256': 'pt', '262': 'tr', '266': 'pt', '274': 'es', '300': 'fr', '307': 'de', '318': 'fr', '325': 'pt', '329': 'fr', '348': 'pt', '350': 'ro', '359': 'it', '363': 'fr', '367': 'es', '380': 'fr', '385': 'es', '389': 'es', '391': 'de', '393': 'de', '409': 'es', '428': 'es', '438': 'es', '453': 'tl', '456': 'fr', '465': 'es', '469': 'fr', '480': 'pt', '484': 'fr', '493': 'es', '513': 'it', '515': 'it', '519': 'es', '524': 'it', '532': 'da', '535': 'de', '536': 'pt', '547': 'fr', '551': 'es', '580': 'ja', '582': 'es', '588': 'es', '590': 'de', '608': 'nl', '614': 'es', '617': 'it', '624': 'es', '629': 'ha', '645': 'es', '647': 'it', '651': 'es', '653': 'is', '666': 'es', '669': 'fr', '673': 'pt', '697': 'co', '704': 'es', '713': 'it', '714': 'fr', '717': 'es', '725': 'es', '741': 'de', '759': 'fi', '761': 'fr', '787': 'pt', '797': 'fr', '798': 'fr', '799': 'ha', '804': 'es', '808': 'es', '823': 'de', '828': 'es', '832': 'de', '833': 'fr', '847': 'fr', '858': 'de', '864': 'es', '878': 'it', '890': 'es', '893': 'es', '913': 'es', '914': 'es', '920': 'es', '940': 'af', '945': 'gd', '951': 'pt', '956': 'es', '959': 'es', '964': 'es', '965': 'es', '976': 'pt', '979': 'de', '986': 'es'}
#non_eng_list = []
#for key,value in non_eng_dict.items():
#    non_eng_list.append(key)
    
lines_dict_trans1 = {}
for key,value in lines_dict.items():
    if key in non_eng_dict:
        lines_dict_trans1[key] = translate_google(value)

file = open('lyrics_translated_temp1.txt','w')
file.write(str(lines_dict_trans1))
file.close()


