import re
import random
from duplicate_mystery_word import *

def get_level_and_word_list():
    level = user_select_level()
    words = get_text(select_word_list())
    clean_word_list = clean_text(words)
    return make_word_list(level, clean_word_list)

def find_longest_word(word_list):
    return len(sorted(word_list, key=len, reverse=True)[0])

def choose_word_length(level, longest_word):
    if level == "e":
        return random.choice([4, 5, 6])
    if level == "m":
        return random.choice([6, 7, 8])
    if level == "h":
        number_list = []
        for i in range(8, longest_word):
            number_list.append(i)
        return random.choice(number_list)

def create_word_list(word_length, word_list):
    new_word_list = []
    for word in word_list:
        if len(word) == word_length:
            new_word_list.append(word)
    return new_word_list

def ask_number_guesses():
    pass

def create_word_families(word_list, guess):  #guess needs to be a list
    """Create word family dictionaries based on a list of words and a new guess"""
    word_family_dict = {}
    for word in word_list:
        if display_word(word, guess) not in word_family_dict.keys():
            word_family_dict[(display_word(word, guess))] = [word]
        else:
            word_family_dict[(display_word(word, guess))].append(word)
    return word_family_dict

def find_largest_word_family(word_family_dictionary):
    """Finds largest word family given dictionary with word family as key and list
        of words as value"""
    most = (sorted(word_family_dictionary.items(), key=lambda x: len(x[1]),
            reverse=True))[0]
    return most




#def make_word_list(level, clean_word_list):
