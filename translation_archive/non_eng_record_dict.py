#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:48:29 2019

@author: wenya
"""

# This is the output of using TextBlob to check the first line of every song, if it's not english, we record the language here
# =============================================================================
# 
# # Check which songs are not in english
# from textblob import TextBlob
# non_eng_record = {}
# for key, value in lines_dict.items():
#     if len(value[0]) >= 3:
#         x = TextBlob(value[0]).detect_language()
#         if x != 'en':
#             non_eng_record[key] = x 
# 
# =============================================================================

non_eng_record = {'016': 'es',
 '023': 'pt',
 '026': 'de',
 '032': 'pt',
 '051': 'es',
 '074': 'zu',
 '082': 'fr',
 '093': 'es',
 '106': 'es',
 '111': 'es',
 '146': 'pt',
 '152': 'es',
 '154': 'it',
 '155': 'es',
 '157': 'pt',
 '170': 'fr',
 '177': 'es',
 '191': 'es',
 '194': 'es',
 '215': 'es',
 '226': 'es',
 '232': 'fr',
 '248': 'es',
 '252': 'fr',
 '256': 'pt',
 '262': 'tr',
 '266': 'pt',
 '274': 'es',
 '300': 'fr',
 '307': 'de',
 '318': 'fr',
 '325': 'pt',
 '329': 'fr',
 '348': 'pt',
 '350': 'ro',
 '359': 'it',
 '363': 'fr',
 '367': 'es',
 '380': 'fr',
 '385': 'es',
 '389': 'es',
 '391': 'de',
 '393': 'de',
 '409': 'es',
 '428': 'es',
 '438': 'es',
 '453': 'tl',
 '456': 'fr',
 '465': 'es',
 '469': 'fr',
 '480': 'pt',
 '484': 'fr',
 '493': 'es',
 '513': 'it',
 '515': 'it',
 '519': 'es',
 '524': 'it',
 '532': 'da',
 '535': 'de',
 '536': 'pt',
 '547': 'fr',
 '551': 'es',
 '580': 'ja',
 '582': 'es',
 '588': 'es',
 '590': 'de',
 '608': 'nl',
 '614': 'es',
 '617': 'it',
 '624': 'es',
 '629': 'ha',
 '645': 'es',
 '647': 'it',
 '651': 'es',
 '653': 'is',
 '666': 'es',
 '669': 'fr',
 '673': 'pt',
 '697': 'co',
 '704': 'es',
 '713': 'it',
 '714': 'fr',
 '717': 'es',
 '725': 'es',
 '741': 'de',
 '759': 'fi',
 '761': 'fr',
 '787': 'pt',
 '797': 'fr',
 '798': 'fr',
 '799': 'ha',
 '804': 'es',
 '808': 'es',
 '823': 'de',
 '828': 'es',
 '832': 'de',
 '833': 'fr',
 '847': 'fr',
 '858': 'de',
 '864': 'es',
 '878': 'it',
 '890': 'es',
 '893': 'es',
 '913': 'es',
 '914': 'es',
 '920': 'es',
 '940': 'af',
 '945': 'gd',
 '951': 'pt',
 '956': 'es',
 '959': 'es',
 '964': 'es',
 '965': 'es',
 '976': 'pt',
 '979': 'de',
 '986': 'es'}

all_language_list = ['en']
for key,value in non_eng_record.items():
    if value not in all_language_list:
        all_language_list.append(value)
all_language_list
len(all_language_list)

## We have 19 unique languages including english, and 117 songs that are not in english



non_eng_dict = {'016': 'es', '023': 'pt', '026': 'de', '032': 'pt', '051': 'es', '074': 'zu', '082': 'fr', '093': 'es', '106': 'es', '111': 'es', '146': 'pt', '152': 'es', '154': 'it', '155': 'es', '157': 'pt', '170': 'fr', '177': 'es', '191': 'es', '194': 'es', '215': 'es', '226': 'es', '232': 'fr', '248': 'es', '252': 'fr', '256': 'pt', '262': 'tr', '266': 'pt', '274': 'es', '300': 'fr', '307': 'de', '318': 'fr', '325': 'pt', '329': 'fr', '348': 'pt', '350': 'ro', '359': 'it', '363': 'fr', '367': 'es', '380': 'fr', '385': 'es', '389': 'es', '391': 'de', '393': 'de', '409': 'es', '428': 'es', '438': 'es', '453': 'tl', '456': 'fr', '465': 'es', '469': 'fr', '480': 'pt', '484': 'fr', '493': 'es', '513': 'it', '515': 'it', '519': 'es', '524': 'it', '532': 'da', '535': 'de', '536': 'pt', '547': 'fr', '551': 'es', '580': 'ja', '582': 'es', '588': 'es', '590': 'de', '608': 'nl', '614': 'es', '617': 'it', '624': 'es', '629': 'ha', '645': 'es', '647': 'it', '651': 'es', '653': 'is', '666': 'es', '669': 'fr', '673': 'pt', '697': 'co', '704': 'es', '713': 'it', '714': 'fr', '717': 'es', '725': 'es', '741': 'de', '759': 'fi', '761': 'fr', '787': 'pt', '797': 'fr', '798': 'fr', '799': 'ha', '804': 'es', '808': 'es', '823': 'de', '828': 'es', '832': 'de', '833': 'fr', '847': 'fr', '858': 'de', '864': 'es', '878': 'it', '890': 'es', '893': 'es', '913': 'es', '914': 'es', '920': 'es', '940': 'af', '945': 'gd', '951': 'pt', '956': 'es', '959': 'es', '964': 'es', '965': 'es', '976': 'pt', '979': 'de', '986': 'es'}
non_eng_list = []
for key,value in non_eng_dict.items():
    non_eng_list.append(key)

# remove 917, this is an english song
