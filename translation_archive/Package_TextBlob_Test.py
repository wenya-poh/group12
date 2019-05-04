#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:15:13 2019

@author: wenya
"""

## Testing TextBlob

## Install TextBlob package. https://github.com/sloria/textblob , https://textblob.readthedocs.io/en/dev/quickstart.html#create-a-textblob
## In Termianl type (1) "pip install -U textblob", then (2) "python -m textblob.download_corpora"
## Classes: https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.tags

from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")
wiki.tags
wiki.noun_phrases # Extract nouns from the text
wiki.words #Extract individual words into a list
wiki.sentiment

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
testimonial.sentiment

w1 = TextBlob("I feel good")
w1.sentiment
w1.detect_language()

w2 = TextBlob("I feel good but this is terible...")
w2.sentiment

w3 = TextBlob("how could this happen to me, I made my mistakes, nowhere to run")
w3.sentiment

w4 = TextBlob("she's such an idiot, why do you trust her?")
w4.sentiment

w5 = TextBlob("They get tired of you and they're gonna put you down (put you down, put you down)")
w5.sentiment

w6 = TextBlob("In fact there's no other girl in this whole wide world who can love you like I do")
w6.sentiment
w6.sentiment[0]


# Test language detection and translation
s152 = TextBlob("Tomame en tus brazos,embriagame de amor")
s152.detect_language()
s152.translate(to='en')

s154 = TextBlob("Bianco e azzurro sei")
s154.detect_language()
s154.translate(to='en')

s170 = TextBlob("Si les Ricains n'étaient pas là")
s170.detect_language()
s170.translate(to='en')

s191 = TextBlob("Sali un dia con mi amigo why su dinero a buscar diversion")
s191.detect_language()
s191.translate(to='en')
x = s191.detect_language()

s256 = TextBlob("Ai Mouraria")
s256.detect_language()

scn = TextBlob("我爱你")
scn.detect_language()
scn.translate(to='en')

scn2 = TextBlob("wo ai ni")
scn2.detect_language()
scn2.translate(to='en')

sen = TextBlob("hello")
sen.detect_language()


#
    #Translation for any song that is not in english
    from textblob import TextBlob
    song_words_translated = []
    for k in song_words:
        if TextBlob(k).detect_language() != 'en':
            w = TextBlob(k).translate(to='en')
            song_words_translated.append(str(w))
#

                if len(word) >= 3 and TextBlob(word).detect_language() != 'en':
                    TextBlob(word).translate(to='en')    
                    
            #if TextBlob(line).detect_language() != 'en':
                #line = str(TextBlob(line).translate(to='en'))