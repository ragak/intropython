def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    values that map to 0 are not included
    '''
    def listnodup(b):
        """
        return unduplicated values in list b
        """
        uniques=[]
        for a in range(len(b)):
            c=b[:]
            test=c.pop(a)
            if test not in c:
                uniques.append(test)
        return uniques
    
    allvals=aDict.values()
    unique=listnodup(allvals)
    tempdict={}
    for a in aDict:
        if aDict[a] in unique:
            tempdict[a]=aDict[a]
    finlist=sorted(tempdict.keys())
    return finlist

