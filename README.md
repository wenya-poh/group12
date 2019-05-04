# GROUP 12 

Members
- Darren Lionel Chan (dgc2136)
- Wenya Poh (wp2254)

Description of Project: 
This project analyzes 1001 song lyrics (txt files) provided in the Tools for Analytics class. 

Dimensions rated:
	• kid_safe: no bad words
		○ 0 is not kid safe
		○ 1 is very kid safe
	• love: is it a love song? 
		○ 0 is not a love song
		○ 1 is a love song
	• mood: Upbeat, has a positive message
		○ 0 is a dark song
		○ 1 is a very happy song
	• length: how long is it
		○ 0 is a short song
		○ 1 is a very long song
	• complexity: requires high level of vocabulary to understand
		○ 0 is a very simple song
		○ 1 is a very complex song

1. How the code works
- main(path) is the function contains all steps to be executed, and produces an output in json format
- Within main(), the code takes the path of the Lyrics folder and does a few treatments, including creation lyric_dict and lines_dict
- lyric_dict: Dictionary of all songs where key = song id, value = list of all words containted within the song
- lines_dict: Dictionary of all songs where key = song id, value = list of all sentences containted within the song
- Please keep translated.py in the same directory as main.py when the code is run for the non-english songs

2. Non-english songs
- There are 116 songs that are not in English.
- Including english, there are 19 unique languages ['en','es','pt','de','zu','fr', 'it', 'tr', 'ro', 'tl', 'da', 'ja', 'nl', 'ha', 'is', 'co', 'fi', 'af', 'gd']
- This was determined using the Google Translate API to check the first sentence of each song file.
- translated.py contains hard-coded translations of the 116 non-english songs. This was handled using GoogleTranslate API to loop through all songs that are non-english, then doing a translation of each of them. 
- The translations are stored locally, and we will not ask markers to run the API in the code, because there will be too many requests needed to translate all 116 songs. We were able to translate 10-18 songs per run of the loop. 
- In main(), after lyric_dict and lines_dict are created, we then cross check with the dictionary of non-english songs (non_eng_dict from translations.py), and replace the specific key-value pairs with the translation
- Files used are in translations_archive folder. Note that translate_songs.py was used to do the translations and store them as dictionaries inside translation.py

3. Scoring:
- The function scaler(max_,min_,value) scales counts accoording to where the value stands between the min and max of the attribute we are measuring. The output is normalized to be between 0 and 1. 

4. Length score
- Counts the absolute number of words contained by each song
- Scores the no. of words for each song against the song with the min and max words in the 1001 songs
- Function detect_length(lyric_dict_, song_ID_sorted_) returns a dictionary with the normalized score of each song

5. Kid Safe score
- Used Google's profanity list to do a scoring of no. of profanity words per song
- Scores the no. of words for each song against the song with the min and max words in the 1001 songs
- function kid(lyric_dict_) returns a dictionary with the normalized score of each song, which is directly reversed from the profanity scoring. 

6. Complexity score
- Requires nltk package
- Checks words against stopwords (simple words), and keeps a count of words that are not simple
- Scores the no. of words for each song against the song with the min and max non-simple words in the 1001 songs
- function detect_complexity(lyric_dict_,song_ID_sorted) returns a dictionary with the normalized score of each song

7. Mood score
- Requires textblob package
- Uses sentiment analysis from textblob to score each word on its polarity (how positive or negative the song is). We find the highest and lowest sentiment score as the max and min boundaries for our scoring of the 1001 songs
- function Mood(lines_dict_) returns a dictionary with the normalized score of each song. 

8. Love score
- Uses a list of words gathered from thesauras and synonyms to do with love and love-related songs
- Code checks the words of each song against the set list and finds the absolute count
- function love(lyric_dict) returns a dictionary with the normalized score of each song. 


Key Package Requirements:
textblob
nltk

