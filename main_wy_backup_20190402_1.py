#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:23:01 2019

@author: wenya
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
    

### DARREN's
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
    
    for line in raw_lines:
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
    

## Doesn't work because it calls GoogleTranslate API too many times
#3 Create the main lyric dictionary with id: [list of song words]
def read_song(txt_name):
    # returns all words for 1 song
    textfile = open(str(txt_name),encoding="utf8")
    raw_lines = []
    song_words = []
    
    for i in textfile:
        # Additional code to handle lines that are not in english, translate to english
        if TextBlob(i).detect_language() != 'en':
            i = TextBlob(i).translate(to='en') 
        raw_lines.append(str(i).split())
    
    for line in raw_lines:
        if line != []:
            for word in line:
                song_words.append(word)
    return song_words


#######
# Backup from 18th April 2019
## Removed the code that makes lyric_dict_lower because lyric_dict now only has lowercase
    
##### Make lyrics_dict_lower
lyric_dict_lower = {}
n=0
while n<=1000:
    lyric_dict_lower[song_ID_sorted[n]] = lyrics_list_lower[n]
    n+=1


##### Gives the list of love_keywords from our CSV
love_keywords = []
love_csv =open('love_keywords.csv',encoding="utf8")
for i in love_csv:
    love_keywords.append(i.strip('\n').rstrip().lower())
    
with open("love_keywords_list.txt", "w") as output:
    output.write(str(love_keywords))



def max_min_love(lyric_dict_):
    # input is the lyric_dict, where each value is a list of all words in 1 song
    # contains a loop that uses detct_love_count function to get the value for every song and appends it to all_love_scores, then we find the max and min
    all_love_scores = []
    love_scores_dict = {}
    for key,value in lyric_dict_.items():
        all_love_scores.append(detect_love_count(value))
        love_scores_dict[key] = detect_love_count(value)
    return love_scores_dict
    #return(max(all_love_scores),min(all_love_scores))
love_scores_dict = max_min_love(lyric_dict)
maxmin_love_score = max_min_love(lyric_dict)

love_dict = {}
for key,value in lyric_dict.items():
    love_dict[key] = scaler(maxmin_love_score[0],maxmin_love_score[1],detect_love_count(value))

