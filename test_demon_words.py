from demon_words import *

word_list = ["river", "divot", "bark", "bank", "rivers", "oceans", "justice", \
            "boolean", "dog", "cat"]

def test_find_longest_word():
    assert find_longest_word(word_list) == 7

def test_choose_word_length():
    assert choose_word_length("e", 15) in [4, 5, 6]
    assert choose_word_length("m", 20) in [6, 7, 8]
    assert choose_word_length("h", 15) in [8, 9, 10, 11, 12, 13, 14, 15]

def test_create_word_list():
    assert len(create_word_list(6, word_list)) == 2
    assert "rivers" in create_word_list(6, word_list)

test_words = ["ally", "beta", "cool", "deal", "else", "flew", "good", "hope", \
                "ibex"]
guess = ["e"]

guess_two_letters = ["e", "o"]

def test_create_word_families():
    assert create_word_families(test_words, guess) == {"_ _ _ _": ["ally",
            "cool", "good"], "_ E _ _": ["beta", "deal"], "_ _ E _": ["flew",
            "ibex"], "E _ _ E": ["else"], "_ _ _ E": ["hope"]}

#    assert create_word_families(test_words, guess_two_letters) == {"_ O O _":
#            ["cool", "good"], "_ _ _ _": ["ally"]}

test_dict = {"first": [1, 2, 3], "second": [1, 2, 3, 4], "third": [1, 2]}

def test_find_largest_word_family():
    assert find_largest_word_family(test_dict) == ("second", [1, 2, 3, 4])
