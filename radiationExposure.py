def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    nextstart=start+step
    area = 0
    if nextstart >= stop+step:
        return area
    else:
        area += f(start)*step + radiationExposure(nextstart, stop, step)
        #print "nextstart is " + str(nextstart)
        #print "f(start) is " + str(f(start))    
        #print "area is " + str(area)
    return area
