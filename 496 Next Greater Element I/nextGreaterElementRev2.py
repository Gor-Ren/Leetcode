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
        For each element in findNums, finds the location of that value in nums
        and searches to the right for the next greater element. Returns a list
        of next greater values for each element in findNums. If greater value
        cannot be found, returns -1 for that element.
        
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Concept: for each element in findNums, find the index of that element
        #   in nums. Search to the right of index in nums for next greater
        #   element. Add it to an output list if found, add -1 if not.
        #   A brute force method.
        #   Rev 1:  improved interpretation of challenge basis...
        #   Rev 2:  improve speed by creating a dictionary of nums element
        #           -index pairs to avoid searching list.
        
        # Initialise list to store next greater values
        greaterValueList = []
        # Initialise dict to store nums element-index pairs
        numsDict = {}

        # Create dict of nums element-index pairs
        for index in range(len(nums)):
            numsDict[nums[index]] = index
        
        # For element in findNums
        for findElement in findNums:
            # Locate the index of where it occurs in nums using dict
            numsIndex = numsDict[findElement]
            # Iterate through elements to the right of index where it occurs
            for numsElement in nums[numsIndex+1:]:
                # If a nums element is greater than the findNums element
                if numsElement > findElement:
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
