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
        # Strategy: iterate through nums, and calculate a running cumulative sum.
        #   Keep track of the highest sum reached, and the range which produced
        #   this best sum. If the sum goes negative at any point, begin summing a 
        #   new range at next element to test for a better sum on a later subarray.
        # Assume nums will always contain at least 1 element.
        
        curSum = 0 # store current sum here
        bestSum = nums[0] # initialise best sum as first element value
        l = 0 # left pointer
        lBest, rBest = 0, 1 # pointers of best sum - initially first element
    
        
        for r in range(len(nums)):
            curSum += nums[r]
            if curSum > bestSum:
                # store value and range of best sum
                bestSum = curSum
                lBest, rBest = l, r
            if curSum <= 0: # <= 0 vs. < 0 thoughts: if curSum is zero there's no 
                            #   point having a bigger subarray for the same sum...
                l = r+1     # start testing for new index range at right
                curSum = 0 # reset sum for new range
        
#        #Test Stuff
#        print("Best range was:\t", nums[lBest:(rBest+1)])
#        print("Best sum:\t", bestSum)
#        return (nums[lBest:rBest+1], bestSum)   
        return bestSum  

### Test Code
#
#import testOutputRev0
#
#test = Solution()
#
#testNo = 1
#
## Example 1
#nums = [-2,1,-3,4,-1,2,1,-5,4]
#
#expect = ([4,-1,2,1], 6)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [0]
#expect = ([0], 0)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [1]
#expect = ([1], 1)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [-1]
#expect = ([-1], -1)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [1, 1]
#expect = ([1, 1], 2)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [-1, 1]
#expect = ([1], 1)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [1, 0, 0, 1]
#expect = ([1, 0, 0, 1], 2)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [2, -1, 0, 3]
#expect = ([2, -1, 0, 3], 4)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [1, -1, 0, 3]
#expect = ([3], 3)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#    
## Example
#nums = [1, 1, -3, 2, 2]
#expect = ([2, 2], 4)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example
#nums = [1, 1, 2, -3, 2, 2]
#expect = ([1, 1, 2, -3, 2, 2], 5)
#output = test.maxSubArray(nums)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
    