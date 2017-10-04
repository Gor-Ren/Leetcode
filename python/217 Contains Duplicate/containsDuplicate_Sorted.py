# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:07:24 2017

@author: renn1995

Given an array of integers, find if the array contains any duplicates. Your 
function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
"""

class Solution(object):
#    def __init__(self):
#        # test code
#        nums = [1, 2, 3, 4, 5, 11, 7]
#        print(self.containsDuplicate(nums))
    
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Concept: Sort the list. Increment through its indices, and check 
        #   whether adjacent values are equal.        
        
        sortedNums = sorted(nums)
        
        for i in range(0,len(nums)-1): # NB stop at penultimate element comparison
            if sortedNums[i] == sortedNums[i+1]:
                return True
        else:
            return False

#test = Solution()