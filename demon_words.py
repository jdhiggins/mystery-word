import re
import random
from duplicate_mystery_word import *

def get_level_and_word_list():
    level = user_select_level()
    words = get_text(select_word_list())
    clean_word_list = clean_text(words)
    new_word_list = create_word_list(level, clean_word_list)
    print("Your word is {} letters long".format(len(new_word_list[0])))
    return new_word_list

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

def create_word_list(level, word_list):
    word_length = choose_word_length(level, find_longest_word(word_list))
    new_word_list = []
    for word in word_list:
        if len(word) == word_length:
            new_word_list.append(word)
    if new_word_list == []:
        return create_word_list(level, word_list)
    return new_word_list


def get_number_guesses(length_word):
    """Gets a number of guesses from the user between word length and 25"""
    guesses = input(("How many guesses would you like? Enter a number " \
                    "between {} and 25: ".format(length_word)))
    if not guesses.isdigit():
        return get_number_guesses(length_word)
    else:
        guesses = int(guesses)
    if guesses < length_word or guesses > 25:
        return get_number_guesses(length_word)
    else:
        return guesses

#def check_word_family(new_family, old_family):


def create_word_families(word_list, guess): #guess needs to be a list
    """Create word family dictionaries based on a list of words, current
    word family and a new guess"""
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
    most = (sorted(word_family_dictionary.items(), key=lambda x: (len(x[1]), x[0]),
            reverse=True))[0]
    most_family = most[0]
    most_family_list = most[1]
    most_family_list.sort()
    largest_family = (most_family, most_family_list)
    return largest_family

def combine_families(current_family, new_family):
    counter = 0
    word_in_list = []
    for letter in current_family:
        word_in_list.append(letter)
    for letter in new_family:
        if letter.isalpha():
            word_in_list[counter] = letter
        counter += 1
    current_family = ("").join(word_in_list)
    return current_family


def find_current_word_family(original_list, guess_list):
    #guesses must be in correctorder
    new_list = original_list
    current_family = display_word(new_list[0], [])
    for guess in guess_list:
        word_family_dict = create_word_families(new_list, guess)
        word_family = find_largest_word_family(word_family_dict)
        new_list = word_family[1]
        new_list.sort()
        new_family = word_family[0]
        current_family = combine_families(current_family, new_family)
    return current_family, new_list

def game():
    while True:
        counter = 0
        guessed_letters = []
        word_list = get_level_and_word_list()
        number_guesses = get_number_guesses(len(word_list[0]))
        word_family = display_word(word_list[0],[])
        while counter < number_guesses:
            print("You have {} guesses left.".format(number_guesses - counter))
            guess = ask_for_a_guess(guessed_letters)
            guessed_letters.append(guess)
            print(guessed_letters)
            new_word_family, new_word_list = find_current_word_family(word_list,
                                                guessed_letters)
            if new_word_family == word_family:
                print("{} is not in the word.".format(guess))
#                print(word_family)
#                print(new_word_family)
                counter += 1
            else:
                print("Good guess!")
                word_family = new_word_family
                print(word_family)
            if "_" not in new_word_family:
                print("You win!")
                counter = number_guesses + 1
            if counter == number_guesses:
                print("Sorry, you lose.  Your word was {}.".format(new_word_list[0]))
        if not play_again():
            break


if __name__ == "__main__":
    game()
