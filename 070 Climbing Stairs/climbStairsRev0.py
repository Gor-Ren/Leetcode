# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:30:45 2017

@author: renn1995

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        Calculates the number of permutations (an integer) of steps that can be
        taken to climb a stair case of n steps, where each individual step may
        be 1 or 2 steps in size.
        
        :type n: int
        :rtype: int
        """
        # Strategy: use a recursive solution with dynamic programming. Noting
        #   our base cases of f(0)=0, f(1)=1, f(2)=2, for each iteration we 
        #   create two recursive branches: one wherein we take 1 step, and another
        #   where we take 2 steps. We would then feed (n-1) or (n-2) as an arg
        #   into the recursive call.
        # Store the number of permutations of steps for each n inside a dict.
        #   Check the dict each iteration for time efficient execution.
        
        # store solutions in dictionary
        solutions = {}
        
        # add base case solutions
        solutions[0] = 0
        solutions[1] = 1
        solutions[2] = 2
        
        if n < 3:
            return solutions[n] # assumes n is not negative
        
        m = 3

        while m <= n:
            # From m total steps, we can take a stride of 1 or 2 first steps.
            #   The total permutations for m can be calculated by the sum of 
            #   permutations of (m-1) and (m-2) steps.
            solutions[m] = solutions[m-1] + solutions[m-2]
            m += 1
        
        return solutions[n]
            
        
            
## Test Code
import testOutputRev0

test = Solution()

testInputs =  [0, 1, 2, 3, 4, 5, 6]
expects =     [0, 1, 2, 3, 5, 8, 13]

for testNo in range(0,len(testInputs)):
    output = test.climbStairs(testInputs[testNo])
    testOutputRev0.testOutput(expects[testNo], output, testNo, testInputs[testNo])
       