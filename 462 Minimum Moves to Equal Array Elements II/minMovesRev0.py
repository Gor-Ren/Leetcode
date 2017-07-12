# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:30:30 2017

@author: renn1995

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.
"""
class Solution(object):
    def minMoves2(self, nums):
        """
        Returns the minimum number of "moves" to make all elements in a list of
        ints have equal value. A "move" is defined as incrementing or
        decrementing an element.
        
        :type nums: List[int]
        :rtype: int
        """
        # Concept: minimise the number of moves by determining the midpoint of
        #   all list values. The minimum will occur when the midpoint is the
        #   median of all elements. Calculate moves by summing the difference 
        #   of each element to the medium.
        # Next steps: avoid sorted solution (n logn time) using quick select
        
        # Sort the list of nums
        nums.sort()
        
        # Determine the value of the median element. If nums has an even number
        #   of elements, we can take either middle value - the code below will 
        #   take upper
        median = nums[(len(nums) // 2)]
        
        # Initialise variable to count number of moves
        moves = 0
        
        # Determine moves by summing difference of each element and the mean
        for e in nums:
            moves += abs(e - median)
            
        return moves
            
## Test Code
import testOutput

test = Solution()

testNo = 1

# Test
nums = [1,2,3]
expect = 2
output = test.minMoves2(nums)
testOutput.testOutput(expect, output, testNo)
testNo += 1

# Test
nums = [0,2,4,5,10,50]
expect = 50
output = test.minMoves2(nums)
testOutput.testOutput(expect, output, testNo)
testNo += 1