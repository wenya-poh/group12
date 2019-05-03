# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:25:03 2019

@author: dlcgx
"""

import main
import unittest

#Test read_song
read_song(r"000~Jerry-Harrison~No-More-Reruns.txt")

class TestRead_Song(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(read_song(r"000~Jerry-Harrison~No-More-Reruns.txt")), list)

    def test_length(self):
        self.assertEqual(len(read_song(r"000~Jerry-Harrison~No-More-Reruns.txt")),369)
        
    def test_lower(self):
        for i in read_song(r"000~Jerry-Harrison~No-More-Reruns.txt"):
            self.assertEqual(i, i.lower())


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestRead_Song)
# Run each test in suite
unittest.TextTestRunner().run(suite)

type(song_ID_list(["000~Jerry-Harrison~No-More-Reruns.txt","001~Dead-Kennedys~Police-Truck"]))

#test song_ID_list

class TestSong_ID(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(song_ID_list(["000~Jerry-Harrison~No-More-Reruns.txt","001~Dead-Kennedys~Police-Truck"])), list)

    def test_song1(self):
        self.assertEqual(song_ID_list(["000~Jerry-Harrison~No-More-Reruns.txt","001~Dead-Kennedys~Police-Truck"])[0],'000')

    def test_song2(self):
        self.assertEqual(song_ID_list(["000~Jerry-Harrison~No-More-Reruns.txt","001~Dead-Kennedys~Police-Truck"])[1],'001')    
        

# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_ID)
# Run each test in suite
unittest.TextTestRunner().run(suite)       
        

#TEST read_song_lines

class TestSong_lines(unittest.TestCase):

    def test_type(self): 
        self.assertEqual(type(read_song_lines(r"000~Jerry-Harrison~No-More-Reruns.txt")), list)

    def test_length(self):
        self.assertEqual(len(read_song_lines(r"000~Jerry-Harrison~No-More-Reruns.txt")),71)
        
    def test_lower(self):
        for i in read_song_lines(r"000~Jerry-Harrison~No-More-Reruns.txt"):
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

    main.main(r"\Users\dlcgx\OneDrive\Desktop\Tools for Analytics\Project\Lyrics")
    def test_type(self): 
        self.assertEqual(type(read_song_lines(r"000~Jerry-Harrison~No-More-Reruns.txt")), list)

    def test_length(self):
        self.assertEqual(len(read_song_lines(r"000~Jerry-Harrison~No-More-Reruns.txt")),71)
        
    def test_lower(self):
        for i in read_song_lines(r"000~Jerry-Harrison~No-More-Reruns.txt"):
            self.assertEqual(i, i.lower())


# Get tests as a test suite
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSong_lines)
# Run each test in suite
unittest.TextTestRunner().run(suite)       
        
        
        
        
        
        
        