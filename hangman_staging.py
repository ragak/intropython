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
            
