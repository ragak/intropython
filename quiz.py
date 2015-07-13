#quiz

x = "pi"
y="pie"
x,y=y,x

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
    
#if x = 16 and b = 2, then the result is 4 - because 2^4=16
            
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if b>x:
        return 0
    elif x==1:
        return 0
    else:
        return (myLog((x/b),b))+1

def lessThan4(aList):
    '''
    aList: a list of strings
    returns: all elements of list with less than 4 elements
    '''
    result=[]
    for words in aList:
        if len(words)<4:
            result.append(words)
    return result
    
#recursive function to sum digits of a non negative integer
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N%10==N:
        return N
    else:
        return N%10 + sumDigits(N/10)
        
#returns a list of keys in aDict with the value target, in increasing order        
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    if bool(aDict)==False:
        return []
    else:
        resultlist=[]
        keys=aDict.keys()
        values=aDict.values()
        for i in range(len(keys)):
            if values[i] == target:
                resultlist.append(keys[i])
        return sorted(resultlist)

#
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    i=0
    while i<len(L):
        #print "i = " + str(L[i])
        if f(L[i]) == False:
            del L[i]
         #   print "L is " + str(L)
        else:
            i=i+1
    return len(L)
    
#this is the test for the above
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a','twelve','xxx','yyy','aaa']
print satisfiesF(L)
print L
#should print
#2
#['a','a']

L = ['a', 'gkkke', 'ddgg']