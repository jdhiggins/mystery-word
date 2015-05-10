import re
import random
from mystery_word import *

def get_level_and_word_list():
    """Asks for user level selection, creates word list and reports on length
    of word chosen"""
    level = user_select_level()
    words = get_text(select_word_list())
    clean_word_list = clean_text(words)
    new_word_list = create_word_list(level, clean_word_list)
    print("Your word is {} letters long".format(len(new_word_list[0])))
    return new_word_list

def find_longest_word(word_list):
    """Finds longest word in a list of words"""
    return len(sorted(word_list, key=len, reverse=True)[0])

def choose_word_length(level, longest_word):
    """Chooses word length based on user-chosen level"""
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
    """Given user level and word list, selects word length and creates word list
    of words of selected length.  If there are no words of that length, prompts
    for new choice"""
    word_length = choose_word_length(level, find_longest_word(word_list))
    new_word_list = []
    for word in word_list:
        if len(word) == word_length:
            new_word_list.append(word)
    if new_word_list == []:
        print("I don't have any words of that length")
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

def create_word_families(word_list, guess): #guess needs to be a list
    """Create word family dictionaries based on a list of words in the current
    word family and a new guess"""
    word_family_dict = {}
    for word in word_list:
        if display_word(word, guess) not in word_family_dict.keys():
            word_family_dict[(display_word(word, guess))] = [word]
        else:
            word_family_dict[(display_word(word, guess))].append(word)
    return word_family_dict

def find_largest_word_family(word_family_dictionary):
    """Finds largest word family given a dictionary with key:word family and
    value: list of words"""
    most = (sorted(word_family_dictionary.items(), key=lambda x: (len(x[1]), x[0]),
            reverse=True))[0]
    most_family = most[0]
    most_family_list = most[1]
    most_family_list.sort()
    largest_family = (most_family, most_family_list)
    return largest_family

def combine_families(current_family, new_family):
    """Adds new letter to old word family to calculate new word family for
    display.  This is used when the user guess is 'correct' and word family
    is changed"""
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
    """Given word list and list of guesses calculates longest current word
    family"""
    #guesses must be in order guessed
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

def game_setup():
    counter = 0
    guessed_letters = []
    word_list = get_level_and_word_list()
    number_guesses = get_number_guesses(len(word_list[0]))
    word_family = display_word(word_list[0],[])
    return (counter, guessed_letters, word_list, number_guesses, word_family)

def game():
    while True:
        (counter, guessed_letters, word_list, number_guesses,
        word_family) = game_setup()
        while counter < number_guesses:
            print("You have {} guesses left.".format(number_guesses - counter))
            guess = ask_for_a_guess(guessed_letters)
            guessed_letters.append(guess)
            print("Your guessed letters are: ", end="")
            for letter in guessed_letters:
                print(letter, end=" ")
            new_word_family, new_word_list = find_current_word_family(word_list,
                                                guessed_letters)
            if new_word_family == word_family:
                print("\n{} is not in the word.".format(guess))
                print(word_family)
                counter += 1
            else:
                print("\nGood guess!")
                word_family = new_word_family
                print(word_family)
            if "_" not in new_word_family:
                print("\nYou win!")
                counter = number_guesses + 1
            if counter == number_guesses:
                print("\nSorry, you lose.  Your word was {}.".format(new_word_list[0]))
                print(new_word_list)
        if not play_again():
            break


if __name__ == "__main__":
    game()
