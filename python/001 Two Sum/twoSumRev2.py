# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:28:18 2017

@author: renn1995
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        Given a list of ints, returns the indices corresponding to the elements
        which sum to the target for the first solution found. If no solution
        found, raises ValueError.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Concept: Iterate through indices of nums, i. Create a dictionary
        #   mapping the element's target complement to its index.
        #   Search nums to find the index of the complement value.
        # Rev 2: perform algorithm in single pass over the list, i.e.
        #   simultaneously build complement dict while checking for solution.
        
        # Create dictionary to map the required complement to indices
        complements = {}
        
        # Iterate through indices of nums
        for j in range(len(nums)):
            # Search complements dict to see if nums[j] is a complement
            i = complements.get(nums[j])
            # If a complement key is found (i =! None), [i, j] is solution 
            if i != None:
                return [i, j]
            # Else (no complement key found), add new complement to dict for j
            else:
                complements[target - nums[j]] = j
                
        # If for loops complete without a solution, raise ValueError
        raise ValueError('No two elements in nums sum to target.')
        