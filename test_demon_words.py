from demon_words import *

word_list = ["river", "divot", "bark", "bank", "rivers", "oceans", "justice", \
            "boolean", "dog", "cat"]

def test_find_longest_word():
    assert find_longest_word(word_list) == 7

def test_choose_word_length():
    assert choose_word_length("e", 15) in [4, 5, 6]
    assert choose_word_length("m", 20) in [6, 7, 8]
    assert choose_word_length("h", 15) in [8, 9, 10, 11, 12, 13, 14, 15]

#def test_create_word_list():
#    assert len(create_word_list(6, word_list)) == 2
#    assert "rivers" in create_word_list(6, word_list)

test_words = ["ally", "beta", "cool", "deal", "else", "flew", "good", "hope", \
                "ibex"]
guess = ["e"]



def test_create_word_families():
    assert create_word_families(test_words, guess) == {"_ _ _ _": ["ally",
            "cool", "good"], "_ E _ _": ["beta", "deal"], "_ _ E _": ["flew",
            "ibex"], "E _ _ E": ["else"], "_ _ _ E": ["hope"]}

#    assert create_word_families(test_words, guess_two_letters) == {"_ O O _":
#            ["cool", "good"], "_ _ _ _": ["ally"]}



#def test_check_number_guesses():
#    assert check_number_guesses(7, "7") == 7
#    assert check_number_guesses(7, "9") == 9
#    assert check_number_guesses(7, "25") == 25

test_dict = {"first": [1, 2, 3], "second": [1, 2, 3, 4], "third": [1, 2]}
test_dict2 = {"_ _ _ _": ["ally", "cool", "good"], "_ E _ _": ["beta", "deal"],
                "_ _ E _": ["flew", "ibex"], "E _ _ E": ["else"],
                "_ _ _ E": ["hope"]}

def test_find_largest_word_family():
    assert find_largest_word_family(test_dict) == ("second", [1, 2, 3, 4])
    assert find_largest_word_family(test_dict2) == ("_ _ _ _", ["ally", "cool",
                                                    "good"])

guess_no_letters = []
guess_one_letter = ["e"]
guess_two_letters = ["e", "o"]
guess_three_letters = ["e", "o", "z"]
guess_four_letters_1 = ["e", "o", "z", "f"]
guess_four_letters_2 = ["e", "o", "z", "c"]
guess_five_letters = ["e", "o", "z", "c", "k"]
guess_six_letters = ["e", "o", "z", "c", "k", "d"]
guess_seven_letters = ["e", "o", "z", "c", "k", "d", "m"]
guess_eight_letters = ["e", "o", "z", "c", "k", "d", "m", "g"]


def test_find_current_word_family():
    assert find_current_word_family(test_words, guess_no_letters) == ("_ _ _ _",
            ["ally", "beta", "cool", "deal", "else", "flew", "good", "hope",
            "ibex"])
    assert find_current_word_family(test_words, guess_one_letter) == ("_ _ _ _",
            ["ally", "cool", "good"])
    assert find_current_word_family(test_words, guess_two_letters) == ("_ O O _",
            ["cool", "good"])
    assert find_current_word_family(test_words, guess_three_letters) == ("_ O O _",
            ["cool", "good"])
    assert find_current_word_family(test_words, guess_four_letters_1) == ("_ O O _",
            ["cool", "good"])
    assert find_current_word_family(test_words, guess_four_letters_2) == ("_ O O _",
            ["good"])
    assert find_current_word_family(test_words, guess_five_letters) == ("_ O O _",
            ["good"])
    assert find_current_word_family(test_words, guess_six_letters) == ("_ O O D",
            ["good"])
    assert find_current_word_family(test_words, guess_seven_letters) == ("_ O O D",
                ["good"])
    assert find_current_word_family(test_words, guess_eight_letters) == ("G O O D",
                ["good"])

def test_combine_families():
    assert combine_families("_ _", "_ A") == "_ A"
    assert combine_families("_ H _", "T _ _") == "T H _"
    assert combine_families("T _ _ T", "_ _ A _") == "T _ A T"
