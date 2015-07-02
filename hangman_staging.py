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
    a=''
    if len(secretWord)==1:
        if secretWord[0] in lettersGuessed:
            return a+secretWord[0]
        else:
            return a + '_ '
    elif len(secretWord)==0:
        return "no secret word"
    else:
        if secretWord[0] in lettersGuessed:
            a += secretWord[0] + ' '
        else:
            a += '_ '
        isWordGuessed(secretWord[1:],lettersGuessed)