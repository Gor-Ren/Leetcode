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
        # Concept: first attempt, try brute force. Take the end of each
        #   interval i, test against all other interval starts, j, to find the
        #   closest start time which is greater than or equal to i's start time.
        
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
        
