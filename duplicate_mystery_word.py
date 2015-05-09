import re
import random

def get_text(text_file):
    """Gets all text from input document."""
    word_list = []
    with open(text_file) as text:
        for word in text:
            word_list.append(word)
    return word_list

def clean_text(word_list):
    """Cleans text from list of words"""
    clean_words = []
    for word in word_list:
        clean_words.append((word.lower()).strip())
    return clean_words

def easy_words(word_list):
    """Returns list of words length 4 to 6 characters from given word list"""
    easy_words = []
    for word in word_list:
        if len(word) > 3 and len(word) < 7:
            easy_words.append(word)
    return easy_words

def medium_words(word_list):
    """Returns list of words length 6 to 8 characters from given word list"""
    medium_words = []
    for word in word_list:
        if len(word) > 5 and len(word) < 9:
            medium_words.append(word)
    return medium_words

def hard_words(word_list):
    """Returns list of words length 8 or more characters from given word list"""
    hard_words = []
    for word in word_list:
        if len(word) > 7:
            hard_words.append(word)
    return hard_words

def random_word(word_list):
    """Chooses a random word from a word list"""
    random_word = random.choice(word_list)
    return random_word

def display_word(word, letter_list):
    """Displays letters already guessed in a word"""
    display = ""
    for letter in word:
        if letter in letter_list:
            display = display + letter.upper() + " "
        else:
            display += "_ "
    display = display[:-1]
    return display

def is_word_complete(word, letter_list):
    """Checks to see if user has guessed all necessary letters to win game."""
    word_letters = []
    for letter in word:
        if letter not in word_letters:
            word_letters.append(letter)
    sorted_word_letters = sorted(word_letters, key=str)
#    print(sorted_word_letters)
    sorted_letter_list = sorted(letter_list, key = str)
#    print(sorted_letter_list)
    if sorted_word_letters == sorted_letter_list:
        return True
    else:
        return False

def user_select_level():
    """Asks user to choose Easy, Medium, or Hard level"""
    good_inputs = ["e", "m", "h"]
    level = (input("Welcome to MYSTERY WORD.  Easy, Medium, or Hard? (E/m/h)?")).lower()
    if level == "":
        return "e"
    elif level not in good_inputs:
        return user_select_level()
    else:
        return level

def pick_word(level, word_list):
    """Picks random word depending on level given word_list"""
    if level == "e":
        word = random_word(easy_words(word_list))
    elif level == "m":
        word = random_word(medium_words(word_list))
    elif level == "h":
        word = random_word(hard_words(word_list))
    else:
        print("Error, level must be e, m, h")
    print("Your word has {} letters.  Good luck\n {}".format
            ((len(word)), display_word(word, [])))
    return word

def ask_for_a_guess(guessed_letters):
    """Asks user for a guess and limits it to one letter character."""
#    print("You have {} guesses left.".format(8 - counter))
    letter = input("Please guess a letter: ")
    if len(letter) != 1:
        print("One letter only please!")
        return ask_for_a_guess(guessed_letters)
    elif letter.lower() in guessed_letters:
        print("Please guess a letter not already guessed.")
        return ask_for_a_guess(guessed_letters)
    elif not letter.isalpha():
        print("Please guess a letter only, no numbers or other.")
        return ask_for_a_guess(guessed_letters)
    else:
        return letter

def guess_check(letter, word):
    """Checks to see if a letter is in a word"""
    word_letters = []
    for item in word:
        if item not in word_letters:
            word_letters.append(item)
    if letter in word_letters:
        return True
    else:
        return False

def select_word_list():
    good_inputs = ["y", "n", ""]
    common = (input("""Would you like to play the kids version? [y/N]: """)).lower()
    if common not in good_inputs:
        return select_word_list()
    if common == "y":
        return("easy_words.txt")
    if common == "n" or common == "":
        return("/usr/share/dict/words")

def get_level_and_pick_word():
    """Gets level information from user and picks an appropriate
    word from our dictionary"""
    level = user_select_level()
#    words = get_text("/usr/share/dict/words")
    words = get_text(select_word_list())
    clean_word_list = clean_text(words)
    return pick_word(level, clean_word_list)

def play_again():
    """Asks user if they would like to play again.  Returns True or False."""
    again = (input("Would you like to play again? [Y/n]: ")).lower()
    if again == "" or again == "y":
        return True
    elif again == "n":
        return False
    else:
        return play_again()

def counter_loop(word, counter, guessed_letters, correct_guessed_letters):
    print("You have {} guesses left.".format(8 - counter))
    guess = ask_for_a_guess(guessed_letters)
    guessed_letters.append(guess)
    if guess_check(guess, word):
        correct_guessed_letters.append(guess)
    else:
        counter += 1
    print(display_word(word, guessed_letters))
    if is_word_complete(word, correct_guessed_letters):
        print("You win!!")
        return 9
    if counter == 8:
        print("Sorry, you lose.  Your word was {}.".format(word))
    return counter

def game():
    while True:
        word = get_level_and_pick_word()
#        print(word)
        counter = 0
        guessed_letters = []
        correct_guessed_letters = []
        while counter < 8:
            counter = counter_loop(word, counter, guessed_letters,
            correct_guessed_letters)
#            print("You have {} guesses left.".format(8 - counter))
#            guess = ask_for_a_guess(guessed_letters)
#            guessed_letters.append(guess)
#            if guess_check(guess, word):
#                correct_guessed_letters.append(guess)
#            else:
#                counter += 1
#            print(display_word(word, guessed_letters))
#            if is_word_complete(word, correct_guessed_letters):
#                print("You win!!")
#                break
#            if counter == 8:
#                print("Sorry, you lose.  Your word was {}.".format(word))
        if not play_again():
            break


if __name__ == "__main__":
    game()
