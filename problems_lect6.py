def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    b=len(aTup)
    if aTup==():
        return ()
    else:
        if b>=0:
            oddtup2 = aTup[:1] + oddTuples(aTup[2:])
            #print "aTup[:1] is ", (aTup[:1])
            #print "aTup[2:] is ", (aTup[2:])
            #print "oddtup2 is ", (oddtup2) 
    return oddtup2 