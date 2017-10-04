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
             
        :type nums: List[int]
        :rtype: int
        """
        # Concept: calculate tHD using the relation that the total hamming 
        #   distance down a single bit of the list of nums (e.g. rightmost bit)
        #   is equal to (no. 0s) * (no. 1s).
        # We assume elements are 30 bits in length (N.B. problem statement
        #   says values are less than 10^9, corresp. to 2**30.)
        # Determine the number of ones in each row by iterating through
        #   each bit and applying a mask. This will zero every row except
        #   the one we're interested in. The statement "if bit & mask" will
        #   return true if there is a one at that bit.
        # Multiply the number of ones and number of zeros for each bit, then
        #   sum to get total HD.
        
        # Initialise total hamming distance, to be summed for all elements
        totalHamDist = 0
        
        # Calculate and store length of nums (no point re-calculating in loop)
        numsLen = len(nums)
        
        # Iterate through 30 bit positions
        for bitPosition in range(30):
            # Create the mask with a one at that bit position (in binary) by
            #   taking 2 ** (bit position)
            mask = 2 ** bitPosition
            # Initialise the count of ones for that bit position
            ones = 0
            # Iterate through each element in nums
            for el in nums:
                # If there is a one at the bit (found by masking element)
                if el & mask:
                    ones += 1
            # Once all elements iterated, calculate the ham dist for that bit
            #   position using the relation (no. ones) * (no. zeroes)
            bitHamDist = ones * (numsLen - ones)
            # Add the ham dist for that bit position to the total
            totalHamDist += bitHamDist
                
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
            