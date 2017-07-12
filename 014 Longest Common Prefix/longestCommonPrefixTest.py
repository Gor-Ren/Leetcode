# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:51:32 2017

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
        
    
    

import longestCommonPrefixRev0

test = Solution()
testNo = 1

# Test 1
strList = []
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test 2
strList = ['edgecase']
expect = 'edgecase'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test 3
strList = ['','']
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['a','a']
expect = 'a'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test 5
strList = ['a','']
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['','ba']
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['ba','b']
expect = 'b'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['qwerty','uiop']
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['','','']
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['de','bc','a']
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['de','','de']
expect = ''
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['thanks','thanks','thanks']
expect = 'thanks'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['thanksyeah','thanksyea','thanksye']
expect = 'thanksye'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['beep','bemep','beep']
expect = 'be'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['beep','beepbeep','beepmeepsleep']
expect = 'beep'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1

# Test
strList = ['beepmeepsleep','beepbeep','beep']
expect = 'beep'
output = test.longestCommonPrefix(strList)
testOutput(expect, output, testNo)
testNo += 1