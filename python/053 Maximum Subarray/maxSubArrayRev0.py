# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:22:11 2017

@author: Gordon

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # Strategy: identify "islands" of consecutive, positive numbers and "bridges"
    #   of consecutive negative numbers. For each island, determine whether it 
    #   results in net gain to bridge it to the next island.
    
    # initialise a counter for "islands" of positive numbers
    islandNo = 0
    bridgeNo = 0
    # store islands in a list of lists
    islands = [[]]
    bridges = [[]]
    
    if nums[0] >= 0:
        isIsland = True # start creating an island initially if first el is pos
    else: # start on bridge
        isIsland = False
    
    for i in len(nums):
        if nums[i] >= 0:
            if isIsland: 
                # append to current island
                islands[islandNo].append(nums[i])
            else: # we have found the end of a bridge
                islands[islandNo].append(nums[i]) # add el to island
                isIsland = True
                bridgeNo += 1
                bridges.append[[]] # append empty list to start next bridge
        else: # number is negative - add to bridge
            if not isIsland: 
                # append to current bridge
                bridges[bridgeNo].append(nums[i])
            else: # we have found end of an island, and can start new bridge
                bridges[bridgeNo].append(nums[i])
                isIsland = False
                islandNo += 1
                islands.append([]) # start next island
        