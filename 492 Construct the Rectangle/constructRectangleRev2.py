# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:26:55 2017

@author: renn1995

Leetcode challenge 492
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        Takes an area, A, as a integer value and returns integers L and W such
        that L * W = A, under the constraints that L must be greater than or
        equal to W. Returns the L, W pair with the smallest difference.
        Assumes A is not greater than 10e+06.
        
        :type area: int
        :rtype: List[int]
        """
        # Strategy: create an initial guess for L equal to the square root of
        #   area (noting that this will start us as close as possible to L = W).
        #   Test this guess for A modulus L equalling zero, which indicates
        #   that we have a solution and can calculate W = A / L. Else, increment
        #   L down and test this new guess.
        # Rev 1: L must lie between the square root of A and A. L m
        # Rev 2: iterate down widths (below square root of A) because
        #   this is a much smaller interval than the values of L, lying
        #   above the square root!
        
        # First guess: take square root of area, L must be greater than W
        #   so round up for L..
        import math
        W = math.floor(area ** 0.5)
        # Termination criteria: when we have found an L which is a factor of A
        while area % W != 0:
            W -= 1
        # Once this loop terminates, return the found solution
        return [int(area/W), int(W)]

## Test Code
test = Solution()


import testOutputRev0

testNo = 1

# Test
areas = [1,2,3,4,5,6,7,8,9,20,23,25,99,100,1000000]
expect = [[1, 1], [2, 1], [3, 1], [2, 2], [5,1], [3,2],[7,1],[4,2],
          [3,3],[5,4],[23,1],[5,5],[11,9],[10,10],[1000,1000]]
          
for i in range(len(areas)):
    output = test.constructRectangle(areas[i])
    testOutputRev0.testOutput(expect[i], output, testNo)
    testNo += 1
