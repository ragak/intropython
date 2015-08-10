def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    values that map to 0 are not included
    '''
    for a in aDict:
        if aDict[a]!=0:
            temp={
            if aDict[a] not in temp.keys():
                temp[a]=aDict[a]
    finlist=list(temp.keys())
    finlist.sort()
    return finlist