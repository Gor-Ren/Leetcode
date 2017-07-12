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
        # Concept: Iterate through each element of nums, i. Test the addition of i
        #   against every other element, j. Return the indices [i, j] for
        #   nums[i] + nums[j] == target.
        
        # Iterate through indices of nums
        for i in range(len(nums)):
            # Iterate through indices to the right of i
            for j in range(i+1, len(nums)):
                # Test if these elements sum to target
                if nums[i] + nums[j] == target:
                    return [i, j]

        # If for loops complete without a solution, raise ValueError
        raise ValueError('No two elements in list nums sum to target.')
        
        # Thoughts on improvement: need to use a dictionary to allow a (near)
        # constant time search for the complement value, target - nums[i].