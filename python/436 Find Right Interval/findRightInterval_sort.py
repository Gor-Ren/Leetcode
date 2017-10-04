# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:47:48 2017

@author: renn1995
"""


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        # Concept: second attempt, reduce time complexity by creating a sorted
        #   list of interval start times prior to searching for the right
        #   interval. Uses own implementation of merge sort for the sake of
        #   practice/ learning/ fun.
        
        # Merge sort
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
                qPairs = pairs[:len(pairs)//2]
                rPairs = pairs[len(pairs)//2:]
            
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
            if q == len(qPairs):
                sortPairs.append(rPairs[r:])
            if r == len(rPairs):
                sortPairs.append(qPairs[q:])
                
            return sortPairs

        # create index-start pairs of all intervals
        intervalStarts = list(enumerate(intervals[i].start for i in range(len(intervals))))
               
            
        
        result = []
        
        for i in range(len(intervals)):
            # Get the end value of our ith interval
            end = intervals[i].end
            # Set a flag for whether we find a second interval with later start
            found = False
            # Iterate over a second index j
            for j in range(len(intervals)):
                # If we find an interval j with a finish greater/equal to our start 
                if (i != j and intervals[j].start >= end):
                    # If this is the first valid result we found (found=False),
                    #   OR if this is 'better' (lower) than one we already found
                    # N.B. that we will short circuit on "not found" to avoid 
                    #   NameError on minStart if this is our first find.
                    if (not found
                        or intervals[j].start < minStart):
                        # store the new 'best' start value and its index j
                        minStart = intervals[j].start
                        minStartIndex = j
                        found = True
            # Once we have tested every j, store the best index in output list
            if found:
                result.append(minStartIndex)
            else:
                result.append(-1)
                
        return result
        
## Testing

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
import testOutput

test = Solution()

testNo = 1

# Example 1
interval1 = Interval(1,2)
intervals = [interval1]

expect = [-1]
output = test.findRightInterval(intervals)
testOutput.testOutput(expect, output, testNo)
testNo += 1

# Example 2
interval1 = Interval(3,4)
interval2 = Interval(2,3)
interval3 = Interval(1,2)
intervals = [interval1, interval2, interval3]

expect = [-1, 0, 1]
output = test.findRightInterval(intervals)
testOutput.testOutput(expect, output, testNo)
testNo += 1

# Example 3
interval1 = Interval(1,4)
interval2 = Interval(2,3)
interval3 = Interval(3,4)
intervals = [interval1, interval2, interval3]

expect = [-1, 2, -1]
output = test.findRightInterval(intervals)
testOutput.testOutput(expect, output, testNo)
testNo += 1
        
