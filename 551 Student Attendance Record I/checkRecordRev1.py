# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:03:14 2017

@author: renn1995

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Concept: crawl down indices of string. Count absences. When a late
        #   is encountered, check whether the next two chars are also laters
        #   (which indicates a fail).
        # Rev 1: added a check whenever an absence for two or more absences. 
        #   This will return false and save time executing the rest of the loop.
        
        absences = 0
        
        for i in range(len(s)):
            if s[i] == 'A':
                absences += 1 # count absences
                if absences == 2:
                    return False
            elif s[i:i+3] == 'LLL': # late three days in a row
                return False
        # if for loops completes, we have not failed on lates.
        #   evaluate whether we have failed on absences and return.
        return True
     
## Test Code
import testOutputRev0

test = Solution()

testInputs = ['',
              'P',
              'A',
              'L',
              'LLL', # 4
              'AA', # 5
              'PPALLPP',
              'PAALPP', # 7
              'PALPPPA', # 8
              'PLLPLLALLPLLPLLP', 
              'PLLLP'] #10
        
expects = [1] * len(testInputs)

for i in [4, 5, 7, 8, 10]:
    expects[i] = 0 # set the expected output to fail for the identified tests

for testNo in range(0,len(testInputs)):
    output = test.checkRecord(testInputs[testNo])
    testOutputRev0.testOutput(expects[testNo], output, testNo, testInputs[testNo])



