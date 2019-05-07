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
    
song_ID_sorted = main.song_ID_list(file_titles)
song_ID_sorted.sort()
lyric_dict = {}
for n in [0,156,641,541,961,1000]:
    lyric_dict[song_ID_sorted[n]] = main.read_song(path+'/'+file_txt_names[n])
    
song_ID_test = ['000','155','540','640','960','999']   


#Test read_song
main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")

class TestRead_Song(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")), list)

    def test_length(self):
        self.assertEqual(len(main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),369)
        
    def test_lower(self):
        for i in main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt"):
            self.assertEqual(i, i.lower())


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRead_Song)
# Run each test in suite
unittest.TextTestRunner().run(suite)


#test song_ID_list

class TestSong_ID(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(main.song_ID_list(["Lyrics/000~Jerry-Harrison~No-More-Reruns.txt","Lyrics/001~Dead-Kennedys~Police-Truck"])), list)

    def test_song1(self):
        self.assertEqual(main.song_ID_list(["Lyrics/000~Jerry-Harrison~No-More-Reruns.txt","Lyrics/001~Dead-Kennedys~Police-Truck"])[0],'000')

    def test_song2(self):
        self.assertEqual(main.song_ID_list(["Lyrics/000~Jerry-Harrison~No-More-Reruns.txt","Lyrics/001~Dead-Kennedys~Police-Truck"])[1],'001')    
        

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_ID)
# Run each test in suite
unittest.TextTestRunner().run(suite)       
        

#TEST read_song_lines

class TestSong_lines(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(main.read_song_lines(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")), list)

    def test_length(self):
        self.assertEqual(len(main.read_song_lines(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),71)
        
    def test_lower(self):
        for i in main.read_song_lines(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt"):
            self.assertEqual(i, i.lower())


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_lines)
# Run each test in suite
unittest.TextTestRunner().run(suite)               


#TEST scaler



class TestScaler(unittest.TestCase):

    def test_even(self): 
        self.assertEqual(main.scaler(100,0,50),0.5)

    def test_odd(self):
        self.assertEqual(main.scaler(3,1,2), 0.5)
        

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestScaler)
# Run each test in suite
unittest.TextTestRunner().run(suite)                       

#test song length


class TestSong_length(unittest.TestCase):

    def test_length(self):
        self.assertEqual(main.detect_length_count(main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),369)
        

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_length)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxminlength 


class TestMax_Min_length(unittest.TestCase):

    def test_length(self):
        self.assertEqual(main.max_min_length(lyric_dict),(369,31))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_length)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test length output


class Testlength(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(main.length(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(main.length(lyric_dict)['000'],1.0)

    def test_2(self):
        self.assertEqual(main.length(lyric_dict)['999'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testlength)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#test kid safe


class Testdetectprofane(unittest.TestCase):

    def test_1(self):
        self.assertEqual(main.detect_profane_count(main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),0)
        
    def test_2(self):
        self.assertEqual(main.detect_profane_count(main.read_song(r"Lyrics/540~The-Exploited~Beat-the-Bastards.txt")),2)
            
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetectprofane)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxmin profanity


class TestMax_Min_length(unittest.TestCase):

    def test_length(self):
        self.assertEqual(main.max_min_profanity(lyric_dict),(2,0))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_length)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test profanity output
class Testkid(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(main.kid(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(main.kid(lyric_dict)['000'],1.0)

    def test_2(self):
        self.assertEqual(main.kid(lyric_dict)['540'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testkid)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#test complexity

class Testdetect_complexity_count(unittest.TestCase):

    def test_1(self):
        self.assertEqual(main.detect_complexity_count(main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),188)
    def test_2(self):
        self.assertEqual(main.detect_complexity_count(lyric_dict['155']),208)

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetect_complexity_count)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxmincomplex 

class TestMax_Min_complexity(unittest.TestCase):

    def test_length(self):
        self.assertEqual(main.max_min_complexity(lyric_dict),(208,22))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_complexity)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test complex output

class Testcomplex(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(main.complexity(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(main.complexity(lyric_dict)['155'],1.0)

    def test_2(self):
        self.assertEqual(main.complexity(lyric_dict)['999'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testcomplex)
# Run each test in suite
unittest.TextTestRunner().run(suite)     


#TEST MOOD
class Testdetect_songmood(unittest.TestCase):

    def test_1(self):
        self.assertEqual(main.detect_song_mood(main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),0.5073768658321502)
    def test_2(self):
        self.assertEqual(main.detect_song_mood(lyric_dict['155']),0.5)

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetect_songmood)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxminmood 


class TestMax_Min_mood(unittest.TestCase):

    def test_length(self):
        self.assertEqual(main.max_min_mood(lyric_dict),(0.525925925925926, 0.49231340763255654))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_mood)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test mood output


class Testmood(unittest.TestCase):

    def test_length(self): 
        self.assertEqual(len(main.mood(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(main.mood(lyric_dict)['960'],1.0)

    def test_2(self):
        self.assertEqual(main.mood(lyric_dict)['540'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testmood)
# Run each test in suite
unittest.TextTestRunner().run(suite)     


#TEST LOVE

class Testdetect_love_count(unittest.TestCase):

    def test_1(self):
        self.assertEqual(main.detect_love_count(main.read_song(r"Lyrics/000~Jerry-Harrison~No-More-Reruns.txt")),60)
    def test_2(self):
        self.assertEqual(main.detect_love_count(lyric_dict['155']),9)

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testdetect_love_count)
# Run each test in suite
unittest.TextTestRunner().run(suite)       

#Test maxmin love

class TestMax_Min_love(unittest.TestCase):

    def test_maxmin(self):
        self.assertEqual(main.max_min_love(lyric_dict),(60,0))
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMax_Min_love)
# Run each test in suite
unittest.TextTestRunner().run(suite)       


#test love output

class Testlove(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(main.love(lyric_dict)),6)
        
    def test_1(self):
        self.assertEqual(main.love(lyric_dict)['000'],1.0)

    def test_2(self):
        self.assertEqual(main.love(lyric_dict)['999'],0)        
       
        
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testlove)
# Run each test in suite
unittest.TextTestRunner().run(suite)     

#json1_data = json.loads(main.main('Lyrics'))["characterizations"]
#
#json.loads(main.main('Lyrics'))["characterizations"][1000]["id"]
# TEST FINAL OUTPUT
class TestOutput(unittest.TestCase):

    
    
    def test_json(self):
        self.assertEqual(type(main.main('Lyrics')),str)
        
    def test_length(self):
        self.assertEqual(len(json.loads(main.main('Lyrics'))["characterizations"]),1001)

    def test_type_dict(self):
        self.assertEqual(type(json.loads(main.main('Lyrics'))["characterizations"][0]),dict)        
       
    def test_song_999_id(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][1000]["id"], "999")        

    def test_song_112_artist(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][113]["artist"], "Sub Focus")

    def test_song_256_title(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][257]["title"], "Ai Mouraria")

    def test_song_413_kid(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][414]["kid_safe"], 1.0)
        
    def test_song_574_love(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][575]["love"], 0.11111111111111105)
    
    def test_song_664_mood(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][665]["mood"], 0.36310853059401493)

    def test_song_794_length(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][795]["love"], 0.2222222222222222)
  
    def test_song_934_complex(self):
        self.assertEqual(json.loads(main.main('Lyrics'))["characterizations"][935]["complexity"], 0.34463276836158196)
  
# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestOutput)
# Run each test in suite
unittest.TextTestRunner().run(suite)     

        
        
        