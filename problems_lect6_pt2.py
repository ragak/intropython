def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    many=0
    ani=[]
    for i in animals:
        ani = ani + aDict.get(i)
    return len(ani)
    
 ##############   
    
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if bool(aDict)==False:
        return None
    else:
        ndic={}
        for i in aDict.keys():
            numb = len(aDict[i])
            ndic[i]=numb
        maxx = max(ndic.values())             #finds the max value
        keys = [x for x,y in ndic.items() if y == maxx]
        return keys[0]
    