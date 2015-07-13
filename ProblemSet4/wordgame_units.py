def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    #if word is an empty string, 0 points
    score=0
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    if word=="":
        #print "no word"
        #print "score is" + str(score)
        return score
    else:
        for i in word:
            score = score + SCRABBLE_LETTER_VALUES.get(i)
        score2 = score*len(word)
        if len(word)==n:
            score2=score2+50
        #print "score is" + str(score2)
        return score2

#this code is given to us
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand



    # TO DO ... <-- Remove this comment when you code this function
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newhand=hand.copy()
    if word=="":
        return hand
    else:
        for i in word:
            if i in newhand:
                newhand[i] = newhand.get(i) - 1
                newhand = {k:v for k,v in newhand.items() if v != 0}
        return newhand


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word in wordList:
        newhand=hand.copy()
        for i in word:
            if i in newhand:
                newhand[i] = newhand.get(i) - 1
                newhand = {k:v for k,v in newhand.items() if v != 0}
            else:
                return False
                #print "False"
                break
        return True
        #print "True"
    else:
        return False
        #print "False"
        

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handlen=sum(v for k,v in hand.items())
    return handlen

    

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    score = 0
    orighandlen=calculateHandlen(hand)
    #print "first call hand is: " + str(hand)
    #print "first call original hand length is: " + str(len(hand))
    # As long as there are still letters left in the hand:        
    while calculateHandlen(hand)>0: 
        # Display the hand
        for i in range(len(hand)):
            showhand=[]
            for k,v in hand.items():
                showhand.extend(k for i in range(v))
        print "Current Hand: " + " ".join([str(x) for x in showhand] )
        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
            # End the game (break out of the loop)
        if word=='.':
            break
        # Otherwise (the input is not a single period):
        	# If the word is not valid:
                    # Reject invalid word (print a message followed by a blank line)
        else:
                if isValidWord(word, hand, wordList)==False:
                    print "Invalid word, please try again."
                    print('')
                # Otherwise (the word is valid):
                    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                    # Update the hand 
                else:
                    score=score+getWordScore(word, orighandlen)
                    #print "original hand length is: " + str(orighandlen)
                    #print "hand length is: " + str(calculateHandlen(hand))
                    #print "output of getWordScore is: " + str(getWordScore(word, orighandlen))
                    #print "score is: " + str(score)
                    print '"' + word + '"' + " earned " + str(getWordScore(word, orighandlen)) + " points. Total: " + str(score) + " points"
                    hand=updateHand(hand, word)
                    #print "new hand length is: " + str(len(hand))
                    #print "new hand is: " + str(hand)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    #print "length of hand outside loop is: " + str(len(hand))
    if len(hand)>0:
        print "Goodbye! Total score: " + str(score) + " points."
    else:
        print "Run out of letters. Total score: " +str(score) + " points."