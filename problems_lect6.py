def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    oddtup=()
    counter=0
    if aTup==():
        return ()
    elif counter>len(aTup):
        return oddtup
    else:
        counter=counter+2
        oddtup += aTup[0] + oddTuples(aTup[counter])
        