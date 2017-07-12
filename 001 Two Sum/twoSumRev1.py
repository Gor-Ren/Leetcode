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
        
        # Create dictionary to map the required complement to indices
        complements = {}
        
        # Iterate through indices of nums
        for index in range(len(nums)):
            # Store required complement as key, and index as value.
            complements[target - nums[index]] = index

        # Second pass - iterate through list (by index)
        for i in range(len(nums)):
            # Search for whether nums[j] is in complement keys
            j = complements.get(nums[i])
            # Check if we got a hit (!= None) and that it is not the element j
            #   itself (noting that i, j must be different)
            if (j != None) and (j != i):
                return [i, j]
            
        # If for loops complete without a solution, raise ValueError
        raise ValueError('No two elements in nums sum to target.')
        