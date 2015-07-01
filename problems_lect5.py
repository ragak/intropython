#use recursive code to calculate powers

#a**n = a*(a**(n-1))
#base case n=0 answer is 1
#base case n=1 answer is a
#recursive (n != 1), return a * recurPower(a,n-1)

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans=1
    if exp==0:
        return ans
    elif exp==1:
        return base
    else:
        base=base*recurPower(base,exp-1)
#        print 'base = ' + str(base)
#        print 'exp = ' + str(exp)
    return base
    


def recurPowerNew(base,exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp==0:
        return 1
    elif exp>0 and exp%2==0:
       base=recurPowerNew(base*base,exp/2)
    elif exp>0 and exp%2==1:
        base=base*recurPowerNew(base,exp-1)
    return base    
    
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x=min(a,b)
    z=min(a,b)
    y=max(a,b)
    print 'x = ' + str(x)
    print 'y = ' + str(y)
    ans=1
    ans2=1
    while ans>0 or ans2>0:
        ans = y%x
        ans2 = z%x
        x=x-1
        #print 'ans = ' + str(ans)
        #print 'x+1 = ' + str(x+1)
    return x+1
    
#write above in recursive
#euclid's algorithm says:
#If b = 0, then the answer is a
#Otherwise, gcd(a, b) is the same as gcd(b, a % b)
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x=min(a,b)
    y=max(a,b)
    if x == 0:
        ans = y
    else:
        ans=gcdRecur(x,y%x)
    return ans
        
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    ans=0
    for c in aStr:
        ans=ans+1
    return ans
    
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    ans = 1
    if aStr=='':
        return 0
    else:
        return ans + lenRecur(aStr[1:])

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    length=len(aStr)
    middle=int(length/2)-1
    print "middle is " + str(middle)
    if aStr=='':
        return False
    elif len(aStr)==1:
        return char==aStr
    elif aStr[middle]==char:
        return True
    else:
        if aStr[middle]<char:
            #print "newstring is " + aStr[middle+1:]
            return isIn(char,aStr[middle+1:])
        elif aStr[middle]>char:
            #print "newstring is " + aStr[:middle]
            return isIn(char,aStr[:middle])
            

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    a=len(str1)
    b=len(str2)
    if a!=b:
        return False
    elif a==1 and b==1 and str1==str2:
        return True
    else:
        return str1[0]==str2[b-1] and semordnilap(str1[1:],str2[:b-1])