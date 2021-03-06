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

#####
            
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

######
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
