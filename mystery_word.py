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
    print("Your word has {} letters.  You have 8 guesses.  Good luck\n {}".format
            ((len(word)), display_word(word, [])))
    return word

def ask_for_a_guess(guessed_letters):
    letter = input("Please guess a letter: ")
    if len(letter) != 1:
        print("One letter only please!")
        return ask_for_a_guess(guessed_letters)
    elif letter in guessed_letters:
        print("Please guess a letter not already guessed.")
        return ask_for_a_guess(guessed_letters)
    elif letter.isdigit():
        print("Please guess a letter only, no numbers or other.")
        return ask_for_a_guess(guessed_letters)
    else:
        return letter

def guess_check(letter, word):
    word_letters = []
    for item in word:
        if item not in word_letters:
            word_letters.append(item)
    if letter in word_letters:
        return True
    else:
        return False





if __name__ == "__main__":
    while True:
        level = user_select_level()
        words = get_text("/usr/share/dict/words")
        clean_word_list = clean_text(words)
        word = pick_word(level, clean_word_list)
        guessed_letters = []
        correct_guessed_letters = []
        counter = 0
        print(word)
        while counter < 8:
            print("You have {} guesses left.".format(8 - counter))
            guess = ask_for_a_guess(guessed_letters)
            guessed_letters.append(guess)
            if guess_check(guess, word):
                correct_guessed_letters.append(guess)
            print(display_word(word, guessed_letters))

            print(guessed_letters)
            if is_word_complete(word, correct_guessed_letters):
                print("You win!!")
                break
# increment counter only for wrong guess            if guess_
            counter += 1
            if counter == 8:
                print("Your word was {}.".format(word))
        play_again = input("Would you like to play again? [Y/n]: ")
        if not play_again:
            break
