# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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
    count=0
    for s in secretWord:
        for lg in lettersGuessed:
            if(s==lg):
                count+=1
                break
    if(count==len(secretWord)):
        return True
    else:
        return False
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    st=''
    for s in secretWord:
        count=0
        for lg in lettersGuessed:
            if(s==lg):
                count+=1
                st+=s
                break
        if(count==0):
            st+='_'
    return st




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc='abcdefghijklmnopqrstuvwxyz'
    st=''
    for char in abc:
        if char not in lettersGuessed:
            st+=char
    return st

    

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
    mistakesMade=0
    secretWord.lower()
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("------------")
    guess=8
    lettersGuessed=[]
    print("You have "+str(guess)+" guesses left")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")    
    while(guess>0 and mistakesMade!=8):
        a=input("Please guess a letter:")
        num=0
        for n in lettersGuessed:
            if a==n:
                guess+=1
                num+=1
                break
        lettersGuessed+=a.lower()
        availableLetters=getAvailableLetters(lettersGuessed)
        count=0
        for s in secretWord:
            if(s==a):
                count+=1
                break
        g=getGuessedWord(secretWord, lettersGuessed)
        if num==1:
            print("Oops! You've already guessed that letter: "+g)     
            print("------------")
        elif count==0:
            mistakesMade+=1
            print("Oops! That letter is not in my word: "+g)
            print("------------")
        elif isWordGuessed(secretWord, lettersGuessed)==True:
            guess+=1
            print("Good guess: "+g)
            print("------------")
            print("Congratulations, you won! ")
            break
        else:
            guess+=1
            print("Good guess: "+g)
            print("------------")
        guess-=1 
        if guess==0:
            print("Sorry, you ran out of guesses. The word was "+secretWord+".")
        else:
            print("You have "+str(guess)+" guesses left")
            print("Available letters: "+availableLetters)   







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
