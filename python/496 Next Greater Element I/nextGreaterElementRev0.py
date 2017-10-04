# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:03:03 2017

@author: renn1995

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s 
elements are subset of nums2. Find all the next greater numbers for nums1's 
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to 
its right in nums2. If it does not exist, output -1 for this number.
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        For each element in findNums, returns the next greater value in nums
        to the right of that findNums element index. Returns a list corresp.
        to each element in findNums. If greater value cannot be found, 
        value for element returned is -1.
        
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Concept: for each index in findNums, search a slice of nums2
        #   beginning at index + 1. Add first value encountered
        #   which is greater than nums1[index] to output list. 
        #   A brute force method.
        
        # Initialise list to store next greater values
        greaterValueList = []
        
        # For index in findNums
        for index in range(len(findNums)):
            # Iterate elements in nums2 from index+1
            for numsElement in nums[index+1:]:
                # If a nums element is greater than the findNums element
                if numsElement > findNums[index]:
                    # Append the value to the list of greater values
                    greaterValueList.append(numsElement)
                    # And break out of nums loop, to iterate to the next
                    #   findNums value
                    break
            # Else (if we exhaust nums elements and no greater value is 
            #   found) (N.B. for-else behaviour)
            else:
                # Append -1 to the list.
                greaterValueList.append(-1)
        
        return greaterValueList
                    
## Test Code
import testOutput

test = Solution()

testNo = 1

# Test
findNums = [4,1,2]
nums = [1,3,4,2]
expect = [-1,3,-1]
output = test.nextGreaterElement(findNums, nums)
testOutput.testOutput(expect, output, testNo)
testNo += 1

# Test
findNums = [2,4]
nums = [1,2,3,4]
expect = [3,-1]
output = test.nextGreaterElement(findNums, nums)
testOutput.testOutput(expect, output, testNo)
testNo += 1
