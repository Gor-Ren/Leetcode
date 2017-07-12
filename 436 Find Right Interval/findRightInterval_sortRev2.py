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
        # Rev 1: Implemented helper functions for better modularity / clarity.
        # Rev 2: Use built-in sort and search functions to improve runtime
        
        # create list of index-start value tuples
        startPairs = list(enumerate([intervals[i].start for i in range(len(intervals)))
        # sort list of tuples by start value
        # TO DO
        startPairs.sort()
                   
        
        # carry out a bisection search of the sorted start pairs to find the index
        #   of the interval where start >= the ith interval's end.
        result = []
        
        # for every interval element
        for i in range(len(intervals)):
            # Store the interval's end value
            end = intervals[i].end
            # define bisection search index range (entire list)
            jUpper = len(sortedStartPairs) - 1
            jLower = 0
            # Edge case: no start value in any interval is >= end value; return -1
            if end > sortedStartPairs[-1][1]:
                result.append(-1)
            else: # not edge case
                # While the bisection search has not converged on solution
                while jUpper - jLower > 1:
                    # Bisect the search range
                    jMid = (jUpper + jLower) // 2
                    # Test whether solution is above or below mid index and 
                    #   modify search range appropriately
                    if sortedStartPairs[jMid][1] < end:
                        jLower = jMid
                    else:
                        jUpper = jMid
                # Append the index (tuple element 0) of jLower
                result.append(sortedStartPairs[jUpper][0])
                
        return result
        
## Testing

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "(" + str(self.start) + "," + str(self.end) + ")"
        
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


        
