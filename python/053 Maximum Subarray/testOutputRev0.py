# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:31:44 2017

@author: renn1995
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
    
## Typical test code - insert in function
    
#import testOutputRev0
#
#test = Solution()
#
#testNo = 1
#
## Example 1
#input1 = [1,2,3]
#input2 = [2]
#
#expect = 1
#output = test.findRadius(input1, input2)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1
#
## Example 2
#input1 = [1,2,3,4]
#input2 = [1,4]
#
#expect = 1
#output = test.findRadius(input1, input2)
#testOutputRev0.testOutput(expect, output, testNo)
#testNo += 1