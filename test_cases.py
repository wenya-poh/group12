# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:25:03 2019

@author: dlcgx
"""

import main
import unittest
import os, sys
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import json



path = "Lyrics" 

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
    
song_ID_sorted = song_ID_list(file_titles)
song_ID_sorted.sort()
lyric_dict = {}
for n in [0,156,641,541,961,1000]:
    lyric_dict[song_ID_sorted[n]] = read_song(path+'/'+file_txt_names[n])
    
song_ID_test = ['000','155','540','640','960','999']   


#Test read_song
read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")

class TestRead_Song(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")), list)

    def test_length(self):
        self.assertEqual(len(read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),369)
        
    def test_lower(self):
        for i in read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt"):
            self.assertEqual(i, i.lower())


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRead_Song)
# Run each test in suite
unittest.TextTestRunner().run(suite)

type(song_ID_list(["Lyrics/000~Jerry-Harrison~No-More-Reruns.txt","001~Dead-Kennedys~Police-Truck"]))

#test song_ID_list

class TestSong_ID(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(song_ID_list(["Lyrics/000~Jerry-Harrison~No-More-Reruns.txt","Lyrics/001~Dead-Kennedys~Police-Truck"])), list)

    def test_song1(self):
        self.assertEqual(song_ID_list(["Lyrics/000~Jerry-Harrison~No-More-Reruns.txt","Lyrics/001~Dead-Kennedys~Police-Truck"])[0],'000')

    def test_song2(self):
        self.assertEqual(song_ID_list(["Lyrics/000~Jerry-Harrison~No-More-Reruns.txt","Lyrics/001~Dead-Kennedys~Police-Truck"])[1],'001')    
        

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_ID)
# Run each test in suite
unittest.TextTestRunner().run(suite)       
        

#TEST read_song_lines

class TestSong_lines(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(read_song_lines(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")), list)

    def test_length(self):
        self.assertEqual(len(read_song_lines(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),71)
        
    def test_lower(self):
        for i in read_song_lines(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt"):
            self.assertEqual(i, i.lower())


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_lines)
# Run each test in suite
unittest.TextTestRunner().run(suite)               


#TEST scaler



class TestScaler(unittest.TestCase):

    def test_even(self): 
        self.assertEqual(scaler(100,0,50),0.5)

    def test_odd(self):
        self.assertEqual(scaler(3,1,2), 0.5)
        

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestScaler)
# Run each test in suite
unittest.TextTestRunner().run(suite)                       

#test song length


class TestSong_length(unittest.TestCase):

    def test_length(self):
        self.assertEqual(detect_length_count(read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),369)
        

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_length)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxminlength 


class TestMax_Min_length(unittest.TestCase):

    def test_length(self):
        self.assertEqual(max_min_length(lyric_dict),(369,31))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_length)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test length output

len(length(lyric_dict))



class Testlength(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(length(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(length(lyric_dict)['000'],1.0)

    def test_2(self):
        self.assertEqual(length(lyric_dict)['999'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testlength)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#test kid safe

detect_profane_count(read_song(r"Lyrics/540~The-Exploited~Beat-the-Bastards.txt"))

class Testdetectprofane(unittest.TestCase):

    def test_1(self):
        self.assertEqual(detect_profane_count(read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),0)
        
    def test_2(self):
        self.assertEqual(detect_profane_count(read_song(r"Lyrics/540~The-Exploited~Beat-the-Bastards.txt")),2)
            
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetectprofane)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxmin profanity

max_min_profanity(lyric_dict)

class TestMax_Min_length(unittest.TestCase):

    def test_length(self):
        self.assertEqual(max_min_profanity(lyric_dict),(2,0))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_length)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test profanity output

kid(lyric_dict)

class Testkid(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(kid(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(kid(lyric_dict)['000'],1.0)

    def test_2(self):
        self.assertEqual(kid(lyric_dict)['540'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testkid)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#test complexity
detect_complexity_count(lyric_dict['155'])

class Testdetect_complexity_count(unittest.TestCase):

    def test_1(self):
        self.assertEqual(detect_complexity_count(read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),188)
    def test_2(self):
        self.assertEqual(detect_complexity_count(lyric_dict['155']),208)

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetect_complexity_count)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxmincomplex 

max_min_complexity(lyric_dict)

class TestMax_Min_complexity(unittest.TestCase):

    def test_length(self):
        self.assertEqual(max_min_complexity(lyric_dict),(208,22))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_complexity)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test complex output

complexity(lyric_dict)



class Testcomplex(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(complexity(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(complexity(lyric_dict)['155'],1.0)

    def test_2(self):
        self.assertEqual(complexity(lyric_dict)['999'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testcomplex)
# Run each test in suite
unittest.TextTestRunner().run(suite)     


#TEST MOOD

detect_song_mood(lyric_dict['000'])

class Testdetect_songmood(unittest.TestCase):

    def test_1(self):
        self.assertEqual(detect_song_mood(read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),0.5073768658321502)
    def test_2(self):
        self.assertEqual(detect_song_mood(lyric_dict['155']),0.5)

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetect_songmood)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxminmood 


class TestMax_Min_mood(unittest.TestCase):

    def test_length(self):
        self.assertEqual(max_min_mood(lyric_dict),(0.525925925925926, 0.49231340763255654))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_mood)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test mood output


class Testmood(unittest.TestCase):

    def test_length(self): 
        self.assertEqual(len(mood(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(mood(lyric_dict)['960'],1.0)

    def test_2(self):
        self.assertEqual(mood(lyric_dict)['540'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testmood)
# Run each test in suite
unittest.TextTestRunner().run(suite)     


#TEST LOVE

detect_love_count(lyric_dict['000'])

class Testdetect_love_count(unittest.TestCase):

    def test_1(self):
        self.assertEqual(detect_love_count(read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),60)
    def test_2(self):
        self.assertEqual(detect_love_count(lyric_dict['155']),9)

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetect_love_count)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxmin love

max_min_love(lyric_dict)

class TestMax_Min_love(unittest.TestCase):

    def test_maxmin(self):
        self.assertEqual(max_min_love(lyric_dict),(60,0))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_love)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test love output

class Testlove(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(complexity(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(love(lyric_dict)['000'],1.0)

    def test_2(self):
        self.assertEqual(love(lyric_dict)['999'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testlove)
# Run each test in suite
unittest.TextTestRunner().run(suite)     



        
        
        