# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

#WORDLIST_FILENAME = "C:\Users\Raga\Documents\Github\intropython\words.txt"
WORDLIST_FILENAME = "/Users/Raga/Desktop/Github/intropython/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(secretWord)==1:
        if secretWord[0] in lettersGuessed:
            return True   
    elif len(secretWord) >= 2:    
        if secretWord[0] in lettersGuessed and isWordGuessed(secretWord[1:],lettersGuessed):
            #print "newsecret is " + secretWord[1:]
            return True
        else:
            return False
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(secretWord)==1:
        if secretWord[0] in lettersGuessed:
            return secretWord[0]
            #print "word is " + secretWord[0]
        else:
            return '_ '
            print "word is " + '_ '
    elif len(secretWord)==0:
        print "no secret word"
    else:
        if secretWord[0] in lettersGuessed:
            return secretWord[0] + ' ' + getGuessedWord(secretWord[1:],lettersGuessed)
            
        else:
            return '_ ' + getGuessedWord(secretWord[1:],lettersGuessed)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet=string.ascii_lowercase
    for letter in alphabet:
        if letter in lettersGuessed:
            #print "letter is " + str(letter)
            alphabet = alphabet.replace(str(letter),'')
            #print "new alphabet is " + str(alphabet.replace(str(letter),''))
    return alphabet 

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses=8
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-------------"
    lettersGuessed=''
    newguess=''
    print "You have " + str(guesses) + " guesses left."
    while guesses>0:
            avail = getAvailableLetters(lettersGuessed)
            print "Available letters: " + str(avail)
            letter = raw_input("Please guess a letter: ")
            guessInLowerCase = letter.lower()
            lettersGuessed += guessInLowerCase
            if isWordGuessed(secretWord, lettersGuessed):
                print "Good guess: " + str(getGuessedWord(secretWord, lettersGuessed))
                print "------------"
                print "Congratulations, you won!"
                break
            elif guessInLowerCase not in avail:
                newguess = getGuessedWord(secretWord, lettersGuessed)
                print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
                print "------------"
                if guesses==1:
                    print "Sorry, you ran out of guesses. The word was " + secretWord 
                    break
                else:
                    print "You have " + str(guesses) + " guesses left."
            elif guessInLowerCase in secretWord:
                newguess = getGuessedWord(secretWord, lettersGuessed)
                print "Good guess: " + str(getGuessedWord(secretWord, lettersGuessed))
                print "------------"
                print "You have " + str(guesses) + " guesses left."
            elif guessInLowerCase not in secretWord:
                newguess = getGuessedWord(secretWord, lettersGuessed)
                print "Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed))
                print "------------"
                if guesses==1:
                    print "Sorry, you ran out of guesses. The word was " + secretWord 
                    break
                else:
                    guesses -= 1
                    print "You have " + str(guesses) + " guesses left."






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)