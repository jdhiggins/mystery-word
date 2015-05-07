import re

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
    easy_words = []
    for word in word_list:
        if len(word) > 3 and len(word) < 7:
            easy_words.append(word)
    return easy_words

def medium_words(word_list):
    medium_words = []
    for word in word_list:
        if len(word) > 5 and len(word) < 9:
            medium_words.append(word)
    return medium_words

def hard_words(word_list):
    hard_words = []
    for word in word_list:
        if len(word) > 7:
            hard_words.append(word)
    return hard_words

if __name__ == "__main__":
    words = get_text("/usr/share/dict/words")
    clean_text = clean_text(words)
    medium_words = medium_words(clean_text)
    print(medium_words)
