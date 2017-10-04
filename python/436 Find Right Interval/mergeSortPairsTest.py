# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:51:10 2017

@author: renn1995

A separate module for the mergeSortPairs for testing purposes.
For the submission to Leetcode this will have to be include in the main function
module.
"""

def mergeSortPairs(pairs):
    '''
    Takes an input list of tuples containing index-value pairs. Returns
    the list of tuples sorted by values in the format:
    [(index0, start0), (index1, start1), ... ]
    
    pairs: list -> tuples -> (int, int)
    returns: list -> tuples -> (int, int)
    '''
    
    # Divide: halve list until it is inherently sorted (0 or 1 elements)
    if len(pairs) <= 1:
        return pairs
    else:
        # Split pairs into upper and lower halves, q and r
        qPairs = pairs[len(pairs)//2:] # lower half
        rPairs = pairs[:len(pairs)//2] # upper half
    
    # Recursively call function to halve pair lists until they are length 0 or 1
    if len(qPairs) > 1:
        qPairs = mergeSortPairs(qPairs)
    if len(rPairs) > 1:
        rPairs = mergeSortPairs(rPairs)

    # Conquer: combine 'upper' and 'lower' lists into sorted list
    sortPairs = []
    # Track current index in upper and lower pair list with q and r
    q = 0
    r = 0
    # while we have not reached the end of our upper or lower pair lists 
    while q < len(qPairs) and r < len(rPairs):
        # compare the values (index 1 element) of pairs q and r
        if qPairs[q][1] < rPairs[r][1]:
            # append the smaller valued pair to the sorted list, increment to next q
            sortPairs.append(qPairs[q])
            q += 1
        else:
            # smaller valued pair must be in 'r' list, append and increment to next r
            sortPairs.append(rPairs[r])
            r += 1
    # once we reach the end of either list of pairs, we exit the while
    #   loop. We can now append all remaining pairs in the other list 
    #   (noting they are themselves sorted)
    # N.B.: must use "extend", not "append" to add elements to list, and not
    #   a list subslice to the list!
    if q == len(qPairs):
        sortPairs.extend(rPairs[r:])
    if r == len(rPairs):
        sortPairs.extend(qPairs[q:])
        
    return sortPairs
    
## Test Code
import testOutput

testNo = 1

# Test
starts = [5, 4, 3, 2, 1, 0]
pairs = list(enumerate(starts))
expect = [(5,0),(4,1),(3,2),(2,3),(1,4),(0,5)]
output = mergeSortPairs(pairs)
testOutput.testOutput(expect, output, testNo)
testNo += 1

# Test
starts = [5, 4, 3, 2, 1, 0, 9, 12, 6]
pairs = list(enumerate(starts))
expect = [(5,0),(4,1),(3,2),(2,3),(1,4),(0,5),(8,6),(6,9),(7,12)]
output = mergeSortPairs(pairs)
testOutput.testOutput(expect, output, testNo)
testNo += 1

# Test
starts = [0]
pairs = list(enumerate(starts))
expect = [(0,0)]
output = mergeSortPairs(pairs)
testOutput.testOutput(expect, output, testNo)
testNo += 1

# Test
starts = [0,0]
pairs = list(enumerate(starts))
expect = [(0,0), (1,0)]
output = mergeSortPairs(pairs)
testOutput.testOutput(expect, output, testNo)
testNo += 1