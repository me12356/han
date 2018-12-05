# Download a dictionary
# see https://stackoverflow.com/questions/18834636/random-word-generator-python
from urllib.request import urlopen
import random

wordsURL = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = urlopen(wordsURL)
wordList = response.read().splitlines()

# Create a new class called hangman
class hangman(object):
    # Initiate our class with some variables
    def __init__(self, lives=10):
        # Choose a random word and make sure it's treated properly as a string
        self.word = random.choice(wordList).decode('UTF-8').lower()
        # Get all unique characters from our word
        self.wordRemaining = list(set(self.word))
        # An empty list of all guesses made
        self.guesses = []
        # The number of lives we'll give the player
        self.lives = lives
        # print the word so we can test properly
        print(self.word)

    # Return True if the player has at least one life and there are characters left to guess
    def isAlive(self):
        return self.lives > 0 and len(self.wordRemaining) > 0

    # Has this character been guessed already?
    def alreadyGuessed(self, guess):
        return guess in self.guesses

    # Print all guessed characters so far
    def printGuesses(self):
        print("You have guessed: ", "".join(self.guesses))

    # Print remaining lives
    def printLives(self):
        print("You have {} lives remaining.".format(self.lives))

    # Print the complete word with any correctly guessed characters
    def printCurrent(self):
        currentString=""
        for character in self.word:
            if character in self.guesses:
                currentString += character
            else:
                currentString += "_"
        print(currentString)

    # Make a guess
    def makeGuess(self, guess):
        # If we haven't already guessed this character
        if not self.alreadyGuessed(guess):
            # Add this character to our guesses
            self.guesses.append(guess)
            # If this character is in the remaining list
            if guess in self.wordRemaining:
                # Remove the character from the remaining list
                self.wordRemaining.remove(guess)
                print("Correct!")
            else:
                print("Incorrect!")
                # Remove a life
                self.lives -= 1
            self.printGuesses()
            self.printCurrent()
            self.printLives()
        # We have already guessed this character
        else:
            # Exit out and ignore this attempt but do not remove a life
            return

# Prompt for a single character input, printing optional string if not a single character
def inputSingleCharacter(prompt, incorrect=""):
    while True:
        answer = input(prompt)
        if len(answer) == 1:
            return answer.lower()
        else:
            print(incorrect)

# Prompt if player would like to play again
def playAgain():
    answer = inputSingleCharacter("Would you like to play again, {}? (y) ".format(playerName), "Please enter y or n")
    if answer in ['y', 'n']:
        return answer == "y"
    else:
        playAgain()

# Player setup

print("Hangman game")

playerName = input("What is your name? ")

# Format the name nicely into the guess
print("Hello, {}, let's play hangman!".format(playerName))

# Loop to continue playing until the player doesn't want to
while True:
    # Instantiate our game
    currentGame = hangman()

    print("Start guessing ...")

    # While we still have lives remaining
    while currentGame.isAlive():
        # Get a single character input
        guess = inputSingleCharacter("Guess a character: ", "Please enter a single character.")
        # Make the guess
        currentGame.makeGuess(guess)

    # See if the player would like to play again
    if playAgain():
        pass
    else:
        break