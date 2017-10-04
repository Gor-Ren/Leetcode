# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:19:17 2017

@author: Gordon

Leetcode 561 "Array Partition I"

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int, the max sum of 
        """
        # Concept: low numbers need to be paired together to "free" larger numbers 
        #   to pair up, such that MIN(a1, b1) is maximised. Therefore, sort the 
        #   numbers and assign pairs (a1, b1), ..., (an, bn) in numerical order.

        sortNums = sorted(nums)
        
        # If we pair each value in ascending order, the sum of the minimum of 
        #   all pairs is equal to the sum of every other element
        pairSum = sum(sortNums[::2]) # N.B. slice defaults to start_index=0
        
        return pairSum
