# Anagram Finder
import os
os.system("cls")

#import word list from NLTK-make sure to pip install NLTK
import nltk
nltk.download('words')
from nltk.corpus import words

#function to check if 2 words are anagrams
def are_anagrams(word1, word2):
    #decide if 2 words are anagrams
    return sorted(word1) == sorted(word2) 

# function to find all anagrams of a word from a list iof dictionary words
def find_anagrams(word, word_list):
    # convert word to lowercase
    word = word.lower()

    #return list of words that are anagrams o fthe inoput word
    return [w for w in word_list if are_anagrams(word, w.lower()) and w.lower() != word]

#define main function
def anagram_solver():
    #create a list of words from nltk
    word_list = words.words()

    #prompt user
    word = input("Enter a word to find it's anagrams: ")

    # find anagrams for the word
    anagrams = find_anagrams(word, word_list)

    #output
    if anagrams:
        print(f"Anagrams of '{word}' are: {', '.join(anagrams)}")
    else:
        print(f"No anagrams found for word '{word}")



#run the thing
anagram_solver()


