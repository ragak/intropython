print "Please think of a number between 0 and 100!"
high = 100
low = 0
guess = (high + low)/2
print "Is your secret number " + str(guess) + "?"
hint=raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')
if hint == 'c':
    print "Game over. Your secret number was: " + str(guess)
else: 
    while hint != 'c':
        if hint == 'h':
            high = guess
            guess = (high + low)/2
            print "Is your secret number " + str(guess) + "?"
            hint=raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')
        elif hint == 'l':
            low = guess
            guess = (high + low)/2
            print "Is your secret number " + str(guess) + "?"
            hint=raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')
        elif hint != 'h' and hint != 'l' and hint != 'c':
            print "Sorry, I did not understand your input."
            print "Is your secret number " + str(guess) + "?"
            hint=raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')
        else:
            break
print "Game over. Your secret number was: " + str(guess)