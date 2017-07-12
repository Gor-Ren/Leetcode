# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:16:38 2017

@author: renn1995

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.
"""
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        Calculates the total hamming distance between all pairs of ints
        given in list nums.
        
        Uses hammingDistance function (solved for a previous challenge) as a 
        helper.
        
        :type nums: List[int]
        :rtype: int
        """
        # Concept: iterate through each element in nums. Calculate the HD to
        #   every other nums element and sum.
        
        # Helper function
        def hammingDistance(x, y):
            """
            Calculates the hamming distance between two integers, defined as the
            number of dissimilar bits in a binary representation of the two ints.
            
            :type x: int
            :type y: int
            :rtype: int
            """
            # Rev 2 Concept: Use bitwise XOR (^) on input ints to get a binary
            #   number where 1s correspond to differences between the binary
            #   representations of x and y. Sum the 1s and output.
            
            # Apply bitwise XOR
            hamDistBin = bin(x ^ y)
            
            # Count 1s to find hamming distance
            hamDist = hamDistBin.count('1')
            
            return hamDist
            
        # Initialise total hamming distance, to be summed for all elements
        totalHamDist = 0
            
        # Iterate through nums elements by index
        for i in range(len(nums)):
            # Iterate through elements to the right of index i call this (element j)
            for el_j in nums[i+1:]:
                # Calculate hamming distance for that pair; add to total
                totalHamDist += hammingDistance(nums[i], el_j)
                
        return totalHamDist
        
## Test Code
import testOutput

test = Solution()

testNo = 1

# Test
nums = [4, 14, 2]
expect = 6
output = test.totalHammingDistance(nums)
testOutput.testOutput(expect, output, testNo)
testNo += 1
            