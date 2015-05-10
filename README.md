# Mystery Word
To run this program open Terminal and enter:
                            python3 mystery_word.py for regular mode OR
                            python3 demon_words.py for demon mode

Mystery Word is a word guessing game.  In regular mode you will have 8
guesses to complete a word. Easy, Medium and Hard mode will change the length of your word, not the relative rarity of the chosen word.  Correct guesses do not count against your guess total.

Demon Mode is ultra difficult.  The rules are the same, but you may need some
extra guesses.  You may select up to 25!

The prompt for kids mode will use the word list located in easy_words.txt
Otherwise the program will run using the word list at `/usr/share/dict/words`

You will be prompted to exit or play again at the end of each game.

If you'd like to exit sooner, please CTRL - C

GOOD LUCK!


## Description

Implement the game of Mystery Word.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* All the basics of Python!

### Performance Objectives

After completing this assignment, you should be able to:

* Create an interactive program.
* Read from a file.
* Choose a random value.
* Keep track of state.
* Test your code.

## Details

### Deliverables

* A Git repo called mystery-word containing at least:
  * a `README.md` file explaining how to run your project
  * a `requirements.txt` file with any third-party packages needed
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 warnings or errors

## Normal Mode

You will implement the game Mystery Word. In your game, you will be playing
against the computer.

The computer must select a word at random from the list of words in the file
`/usr/share/dict/words`. This file exists on your computer already.

The game must be interactive; the flow of the game should go as follows:

1. Let the user choose a level of difficulty at the beginning of the program.
Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
characters; hard mode only has words of 8+ characters.

2. At the start of the game, let the user know how many letters the computer's
word contains.

3. Ask the user to supply one guess (i.e. letter) per round. This letter can be
upper or lower case and it should not matter. If a user enters more than one
letter, tell them the input is invalid and let them try again.

4. Let the user know if their guess appears in the computer's word.

5. Display the partially guessed word, as well as letters that have not been
guessed. For example, if the word is BOMBARD and the letters guessed are a, b,
and d, the screen should display:

```
B _ _ B A _ D
```

A user is allowed 8 guesses. Remind the user of how many guesses they have left
after each round.

*A user loses a guess only when they guess incorrectly.* If they guess a letter
that is in the computer's word, they do not lose a guess.

If the user guesses the same letter twice, do not take away a guess. Instead,
print a message letting them know they've already guessed that letter and ask
them to try again.

The game should end when the user constructs the full word or runs out of
guesses. If the player runs out of guesses, reveal the word to the user when
the game ends.

When a game ends, ask the user if they want to play again. The game begins
again if they reply positively.

## Hard Mode

Implement the [evil version of this game](http://nifty.stanford.edu/2011/schwarz-evil-hangman/).
Put it in a new Python program called "demon_words.py".

You must write tests for new functionality you introduce.

## Notes

This is the first assignment where you are writing code to make tests pass.
That makes it extra challenging.

When testing, keep in mind that testing user input and output is hard. Testing
functions that have no side-effects -- that is, they take some arguments and
return a value without getting information from `input()` or using `random` --
is much easier. Try to keep all your logic in _pure functions_ and then have an
outer crust of functions that talk to the user or read from files surrounding
your delicious pure function middle. If you are able to do this, you will not
need to test that outer crust.

## Additional Resources

* [nose]https://nose.readthedocs.org/en/latest/).
* [Working with Text Files](https://opentechschool.github.io/python-data-intro/core/text-files.html)

## Credit

This lab is based off a similar exercise in MIT's 6.00.1x course.
