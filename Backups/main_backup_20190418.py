#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:35:30 2019

@author: wenya, darren

Backup is done for the file before lyric_dict_lower is removed

"""

#1 Make list of all lyric text titles
import os, sys

# Language
## Install TextBlob package. https://github.com/sloria/textblob , https://textblob.readthedocs.io/en/dev/quickstart.html#create-a-textblob
## In Termianl type (1) "pip install -U textblob", then (2) "python -m textblob.download_corpora"
## Classes: https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.tags
from textblob import TextBlob


## Change working directory to the folder CONTAINING "lyrics" here - gives list of names of each file
path = "lyrics" ##NOTE: Prof says we will need to use an argparse thing instead of absolute path
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

song_ID_sorted = song_ID_list(file_titles)
song_ID_sorted.sort()
 

# Create the main lyric dictionary with individual words. format is id: [list of song words]
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


# Create the main line dictionary with sentences. format is id: [list of lyric sentences]
## Function to return a list of songs with each line as a string
def read_song_lines(txt_name):
    # returns the first line of each song
    textfile = open(str(txt_name),encoding="utf8")
    raw_lines = []
    for i in textfile:
        raw_lines.append(i.strip('\n').rstrip().lower())
    return raw_lines
## Ensure that file_txt_names was mined from the fist set of code on top first. 
## Change working directory INTO the lyrics folder before running the next few lines
lines_dict = {}
n=0
while n<=1000:
    lines_dict[song_ID_sorted[n]] = read_song_lines(file_txt_names[n])
    n+=1

# Check which songs are not in english
from textblob import TextBlob
non_eng_record = {}
for key, value in lines_dict.items():
    if len(value[0]) >= 3:
        x = TextBlob(value[0]).detect_language()
        if x != 'en':
            non_eng_record[key] = x 
### non_eng_record dictionary is saved in non_eng_record_dict.py for backup record, because GoogleTranslate API may not always be available 

## Obtain list of all indexes that are not in English
non_eng_indexes = []
for key,value in non_eng_record.items():
    non_eng_indexes.append(key)

## translate_list iterates over a list of strings and translates them using TextBlob
def translate_list(list_):
    from textblob import TextBlob
    translated = []
    for i in list_:
        t = TextBlob(str(i)).translate(to='en')
        translated.append(str(t))
    return translated
    
lines_dict_trans = lines_dict
for index in non_eng_indexes:
    lines_dict_trans[index] = translate_list(lines_dict[index])
###WENYA: WORK INPROGRESS. API stops working after the first paragraph of the first song is translated, see the non_eng_record_dict.py


# Generic Functions for scoring:
## Generic scaling function. Returns one scaled value from 0-1.
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
    
## Use TextBlob's sentiment to check polarity - positive or negative.
## Needs to detect sentence by sentence, not by individual words -> use lines_dict
## We use textblob's sentiment detector (built on training set of movie reviews) -> Return a tuple of form (polarity, subjectivity ) where polarity is a float within the range [-1.0, 1.0] and subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
## Our Mood score goes from 0 (most negative mood) to 1 (most positive mood)
from textblob import TextBlob

def detect_song_mood(lines):
    #input: lines is a list of all sentences in 1 song
    mood_score_list = []
    for sentence in lines:
        scaled_sentiment = scaler(1,-1,TextBlob(sentence).sentiment[0]) #Scale textblob's sentiment output from their scale of 1,-1 to our scale of 1,0
        mood_score_list.append(scaled_sentiment)
    mood_score = sum(mood_score_list)/len(mood_score_list)
    return mood_score

def max_min_mood(lines_dict_):
    # input: dictionary of all the lines of songs
    all_mode_scores = []
    for key,value in lines_dict_.items():
        all_mode_scores.append(detect_song_mood(value))
    return(max(all_mode_scores),min(all_mode_scores))
maxmin_mood_score = max_min_mood(lines_dict)

mood_dict = {}
for key,value in lines_dict.items():
    mood_dict[key] = scaler(maxmin_mood_score[0],maxmin_mood_score[1],detect_song_mood(value))



# CODE FOR LOVE
    
## Function that takes a list of words (of a song) and outputs the total love-related songs the song contains
def detect_love_count(words):
    #input: words is a list of all words in one song
    ## list of keywords related was compiled from https://www.thesaurus.com/browse/love + other sources + all pronouns to do with he/she/us/they/you
    love_keywords = ['admire', 'admired', 'admirer', 'adoration', 'adore', 'adored', 'adulate', 'adulation', 'affection', 'allegiance', 'always', 'amity', 'amorousness', 'amour', 'angel', 'applause', 'appreciation', 'approbation', 'approval', 'ardency', 'ardor', 'arms', 'attach', 'attached', 'attachment', 'attract', 'attracted', 'attraction', 'babe', 'baby', 'beau', 'beautiful', 'beauty', 'bed', 'bedded', 'beloved', 'blind', 'body', 'boy', 'boyfriend', 'boys', 'break', 'breakup', 'broken', 'burn', 'burned', 'burning', 'bye', 'call', 'canonize', 'captivated', 'care', 'caress', 'caring', 'case', 'celebrate', 'chance', 'charm', 'charmed', 'charms', 'cheeks', 'cherish', 'cherished', 'cherishing', 'choose', 'choosing', 'chose', 'clasp', 'cling', 'clinging', 'clingy', 'close', 'closer', 'confront', 'confronted', 'cosset', 'court', 'courter', 'crazy', 'cried', 'cries', 'crush', 'crushed', 'crushing', 'cry', 'cuddle', 'dance', 'danced', 'dancing', "darlin'", 'darling', 'dear', 'dear one', 'dearest', 'dearie', 'deference', 'deify', 'delight', 'delighted', 'delighting', 'devoted', 'devotedness', 'devotion', 'dirty', 'divine', 'divinely', 'do', 'dote', 'draw', 'dream', 'dreaming', 'dreams', 'dreamt', 'dude', 'embrace', 'embraced', 'emo', 'emotion', 'enamored', 'enchant', 'enchanted', 'enchantment', 'ended', 'endless', 'enjoy', 'enjoyment', 'esteem', 'esteemed', 'estimation', 'exalt', 'exalted', 'exception', 'eyes', 'fall', "fallin'", 'falling', 'family', 'fancy', 'fascinated', 'fast', 'favor', 'feel', "feelin'", 'feeling', 'female', 'fervor', 'fidelity', 'flame', 'flamed', 'fling', 'flirt', 'flirty', 'fond', 'fondle', 'fondness', 'fool', 'foolish', 'foolishly', 'forever', 'friend', 'friendly', 'friendship', 'friendzone', 'gal', 'gals', 'gaze', 'girl', 'girlfriend', 'girlfriends', 'girls', 'glorification', 'glorify', 'glory', 'go', 'gone', 'goodby-eye', 'goodbye', 'goodnight', 'groom', 'hair', 'hand', 'hands', 'hankering', 'happiness', 'happy', 'he', 'heart', 'heartened', 'high', 'hold', 'homage', 'home', 'honey', 'honor', 'honour', 'hot', 'house', 'hug', 'hugged', 'hugging', 'husband', 'hush', 'idol', 'idolatry', 'idolization', 'idolize', 'inamorata', 'inamorato', 'inclination', 'infatuated', 'infatuation', 'involved', 'involvement', 'joined', 'juliet', 'kiss', 'kissed', 'kissing', 'kissy', 'lady', 'last', 'lay', 'leave', 'leaving', 'lick', 'like', 'liked', 'liking', 'lips', 'long', 'longing', 'love', 'loved', 'lovely', 'lover', 'loving', 'loyal', 'loyalty', 'lust', 'mad', 'magnificant', 'make', 'male', 'man', 'marriage', 'married', 'marry', 'marrying', 'marveling', 'me', 'mine', 'moan', 'moaning', 'neck', 'need', 'needed', 'night', 'nightly', 'obeisance', 'one', 'over', 'paramour', 'part', 'parted', 'partiality', 'passion', 'passionate', 'pedestal', 'perfect', 'pet', 'piety', 'please', 'pleased', 'pleasure', 'praise', 'prefer', 'preferred', 'press', 'pretty', 'prize', 'prized', 'prizing', 'promised', 'promises', 'promising', 'puppy', 'racing', 'rapture', 'recognition', 'regard', 'relation', 'relationship', 'relish', 'respect', 'reverence', 'romance', 'romantic', 'romeo', 'rouse', 'roused', 'secret', 'sentiment', 'sentimental', 'sex', 'sexy', 'she', 'shine', 'significant', 'skin', 'snuggle', 'soft spot', 'somebody', 'someone', 'soothe', 'soul', 'spark', 'sparks', 'stroke', 'sugar', 'suited', 'suitor', 'swain', 'swear', 'swearing', 'sweet', 'sweetheart', 'sweetie', 'swore', 'taken', 'taste', 'tasted', 'tastes', 'tender', 'tenderly', 'tenderness', 'they', 'thrive', 'thump', 'together', 'tonight', 'touch', 'touched', 'touching', 'treasure', 'truelove', 'tryst', 'two', 'us', 'valentine', 'valuing', 'venerate', 'veneration', 'wait', 'waiting', 'want', 'weakness', 'wed', 'wedding', 'wife', 'wild', 'wildest', 'wine', 'woman', 'wonder', 'wonderment', 'woo', 'wooing', 'world', 'worship', 'worshiped', 'worshipping', 'yearning', 'you', 'young', 'yourself', 'zeal']
    love_count = 0
    for i in words:
        if str(i) in love_keywords:
            love_count += 1
    return love_count

## Function that runs through all song words and finds the min and max count for love-related words
def max_min_love(lyric_dict_):
    # input is the lyric_dict, where each value is a list of all words in 1 song
    # contains a loop that uses detct_love_count function to get the value for every song and appends it to all_love_scores, then we find the max and min
    all_love_scores = []
    #love_scores_dict = {}
    for key,value in lyric_dict_.items():
        all_love_scores.append(detect_love_count(value))
        #love_scores_dict[key] = detect_love_count(value)
    #return love_scores_dict
    return(max(all_love_scores),min(all_love_scores))
maxmin_love_score = max_min_love(lyric_dict)

love_dict = {}
for key,value in lyric_dict.items():
    love_dict[key] = scaler(maxmin_love_score[0],maxmin_love_score[1],detect_love_count(value))


# ALWAYS RUN LAST! Create final output dictionary(extract id, artist, title) 
    
def extract_(titles):
    list_1 = []
    for i in titles:
        b = i.split('~')   
        dict_1 = {"id" : b[0], "artist" : b[1], "title" : b[2], 'kid_safe': profanity_dict[b[0]], 'love': love_dict[b[0]], 'mood': mood_dict[b[0]], 'length': length_dict[b[0]], 'complexity': complexity_dict[b[0]]}
        list_1.append(dict_1)
    return list_1
    
output_list = extract_(file_titles)

output_list[983] 


## Notes
# Lyric filenames go from 000 to 1000
# .splitlines() to get each line in a nested list

# Outstanding issues
## Translation
## some txt files say just [Instrumental]
## love score is not counting the UNIQUE love words, but absolute count of love-related words per song. But should be reasonable, the more intense it is the more they will repeat the words.