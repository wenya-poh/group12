#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:35:30 2019

@author: wenya, darren
"""

#1 Make list of all lyric text titles
import os, sys
from textblob import TextBlob

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



# Function to return a list of songs with each line as a string
def read_song_lines(txt_name):
    # returns the first line of each song
    textfile = open(str(txt_name),encoding="utf8")
    raw_lines = []
    for i in textfile:
        raw_lines.append(i.split())
    return raw_lines

# Run through all files and capture the 
foreign_song_ID = []



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
            
            #if TextBlob(line).detect_language() != 'en':
                #line = str(TextBlob(line).translate(to='en'))
            
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

## Create Lyrics List for songs
lyrics_list_lower = []

for i in range(len(lyric_dict)):
    song_list_lower = [] 
    for j in range(len(lyric_dict[song_ID_sorted[i]])):
        song_list_lower.append(lyric_dict[song_ID_sorted[i]][j].lower())
    
    lyrics_list_lower.append(song_list_lower)    

    
# Language
## Install TextBlob package. https://github.com/sloria/textblob , https://textblob.readthedocs.io/en/dev/quickstart.html#create-a-textblob
## In Termianl type (1) "pip install -U textblob", then (2) "python -m textblob.download_corpora"
## Classes: https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.tags
from textblob import TextBlob

  

#### Generic Functions for scoring:

#Generic scaling function. Returns one scaled value from 0-1.
def scaler(max_,min_,value):
    
    x =((1-0)/(max_-min_)*(value-max_)+1) 
    return x 

#CODE FOR SONG LENGTH

#create list of song lengths to find max and min
song_length_list = []
n = 0
while n<=1000:
    song_length_list.append(len(lyric_dict[song_ID_sorted[n]]))
    n+=1


#create dictionary consisting id, song length
length_dict = {}
n = 0
while n<=1000:
    length_dict[song_ID_sorted[n]] = scaler(max(song_length_list), min(song_length_list),len(lyric_dict[song_ID_sorted[n]]))
    n +=1



# CODE FOR KID SAFE
    
profanity_list = ['4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses', 'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'ballbag', 'balls', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bloody', 'blow job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum', 'bunny fucker', 'butt', 'butthole', 'buttmuch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet muncher', 'cawk', 'chink', 'cipa', 'cl1t', 'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck ', 'cocksucked ', 'cocksucker', 'cocksucking', 'cocksucks ', 'cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot', 'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick ', 'cuntlicker ', 'cuntlicking ', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck ', 'cyberfucked ', 'cyberfucker', 'cyberfuckers', 'cyberfucking ', 'd1ck', 'damn', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates ', 'ejaculating ', 'ejaculatings', 'ejaculation', 'ejakulate', 'f u c k', 'f u c k e r', 'f4nny', 'fag', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio', 'fingerfuck ', 'fingerfucked ', 'fingerfucker ', 'fingerfuckers', 'fingerfucking ', 'fingerfucks ', 'fistfuck', 'fistfucked ', 'fistfucker ', 'fistfuckers ', 'fistfucking ', 'fistfuckings ', 'fistfucks ', 'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 'fuckers', 'fuckhead', 'fuckheads', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme ', 'fucks', 'fuckwhit', 'fuckwit', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux', 'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged ', 'gangbangs ', 'gaylord', 'gaysex', 'goatse', 'God', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex ', 'hell', 'heshe', 'hoar', 'hoare', 'hoer', 'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off ', 'jackoff', 'jap', 'jerk-off ', 'jism', 'jiz ', 'jizm ', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked ', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking ', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers ', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'numbnuts', 'nutsack', 'orgasim ', 'orgasims ', 'orgasm', 'orgasms ', 'p0rn', 'pawn', 'pecker', 'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses ', 'pissflaps', 'pissin ', 'pissing', 'pissoff ', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks ', 'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys ', 'rectum', 'retard', 'rimjaw', 'rimming', 's hit', 's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter', 'shitters ', 'shitting', 'shittings', 'shitty ', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated', 'xxx']

profanity_count = []
for i in lyrics_list_lower:
    b = 0
    for j in i: 
        if j in profanity_list:
            b += 1
        else:
            pass
    profanity_count.append(b)
    

## Scale simple word count to 0-1 for kid-friendliness
profanity_dict = {}

n = 0
while n<=1000:
    profanity_dict[song_ID_sorted[n]] = scaler(max(profanity_count),min(profanity_count),profanity_count[n])
    n +=1   



# CODE FOR COMPLEXITY


##### Make lyrics_dict_lower
    
lyric_dict_lower = {}
n=0
while n<=1000:
    lyric_dict_lower[song_ID_sorted[n]] = lyrics_list_lower[n]
    n+=1

##### Remove stop words
import nltk
from nltk.corpus import stopwords


example_sent = "This is a sample sentence, showing off the stop words filtration."
  
stop_words = set(stopwords.words('english')) 

simple_lyrics_list = []

for i in range(len(lyric_dict)):
    
    filtered_sentence = [] 
    
    filtered_sentence = [w for w in lyric_dict_lower[song_ID_sorted[i]] if not w in stop_words] 
  
    for w in lyric_dict_lower[song_ID_sorted[i]]: 
        if w not in stop_words: 
          filtered_sentence.append(w)
    simple_lyrics_list.append(filtered_sentence)
    
## Obtain count of words as proxy for complexity
simple_lyrics_count = []
        
for i in range(len(simple_lyrics_list)):

    x = len(set(simple_lyrics_list[i]))
    simple_lyrics_count.append(x)

## Scale simple word count to 0-1 for complexity
complexity_dict = {}
n = 0
while n<=1000:
    complexity_dict[song_ID_sorted[n]] = scaler(max(simple_lyrics_count), min(simple_lyrics_count),simple_lyrics_count[n])
    n +=1   
    


   

# CODE FOR MOOD
from textblob import TextBlob




# CODE FOR LOVE



#5 ALWAYS RUN LAST! Create final output dictionary(extract id, artist, title) 
    
def extract_(titles):
    list_1 = []
    for i in titles:
        b = i.split('~')   
        dict_1 = {"id" : b[0], "artist" : b[1], "title" : b[2], 'kid_safe': profanity_dict[b[0]], 'love': 0, 'mood': 0, 'length': length_dict[b[0]], 'complexity': complexity_dict[b[0]]}
        list_1.append(dict_1)
    return list_1
    
output_list = extract_(file_titles)

output_list[1] 


## Notes
# Lyric filenames go from 000 to 1000
# .splitlines() to get each line in a nested list