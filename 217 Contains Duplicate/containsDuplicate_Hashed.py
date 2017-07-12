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
#        nums = [1, 2, 3, 4, 5, 2, 7]
#        print(self.containsDuplicate(nums))
    
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Concept: Initialise a set. Iterate through list elements. Check if
        #   each element is in set: if true, it's a duplicate; return True.
        #   If el not in set, add to set and incremenet. 
        
        checkSet = set()
        
        for num in nums:
            if num in checkSet:
                return True
            else:
                checkSet.add(num)
        # if for loop completes without a num in the check set, we can return
        #   False (no duplicates found)
        return False

#test = Solution()