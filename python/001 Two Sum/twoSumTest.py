# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:51:32 2017

@author: renn1995

Tests twoSum algorith
"""

def testOutput(expected, actual, testNo):
    '''
    Tests whether input lists are equal, and prints test result accordingly.
    
    expected: list -> ints
    actual: list -> ints
    returns nothing.
    '''
    if expected == actual:
        print('PASS Test ' + str(testNo))
    else:
        print('FAIL Test ' + str(testNo))
        
    print('\tExpected output:\t', expected)
    print('\tActual output:\t\t', actual)
        
    
    

import twoSumRev2

test = Solution()
testNo = 1

# Test 1: Inputs are zeroes
nums = [0,0]
target = 0
expect = [0, 1]
output = test.twoSum(nums, target)
testOutput(expect, output, testNo)
testNo += 1

# Test 2: Solution elements are same value
nums = [1,0,1]
target = 2
expect = [0, 2]
output = test.twoSum(nums, target)
testOutput(expect, output, testNo)
testNo += 1

# Test 3: Solution elements are non-identical, i = 0
nums = [2,1,9,4]
target = 6
expect = [0, 3]
output = test.twoSum(nums, target)
testOutput(expect, output, testNo)
testNo += 1

# Test 4: i > 0
nums = [3,2,1,1,7,5,2]
target = 7
expect = [1, 5]
output = test.twoSum(nums, target)
testOutput(expect, output, testNo)
testNo += 1

# Test 5: Solution nums are negative
nums = [3, 7, -1, 4, -2, 8]
target = -3
expect = [2, 4]
output = test.twoSum(nums, target)
testOutput(expect, output, testNo)
testNo += 1

# Test 6: Target is double first element.
nums = [1, 4, 2, 3, 4, 0]
target = 8
expect = [1, 4]
output = test.twoSum(nums, target)
testOutput(expect, output, testNo)
testNo += 1

# Test 7: Big ints.
nums = [100, 444, 205, 388, 4000, 99, 8, 52, 174, 168]
target = 4052
expect = [4, 7]
output = test.twoSum(nums, target)
testOutput(expect, output, testNo)
testNo += 1

