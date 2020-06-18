import string
import random

def load_words():
    """
    this function will help to load more words
    """

    WORDLIST_FILENAME =("words.txt")
    inFile = open(WORDLIST_FILENAME)
    line = inFile.readline()
    word_list = line.split()  
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    this function will return randomly one word
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word