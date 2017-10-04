# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:45:51 2017

@author: renn1995
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # Strategy: For each house, find the distance of the closest heater.
        #   The maximum distance of closest heater across all houses is the 
        #   required radius.
                  
        result = 0
                                                       
        for house in houses:
            # create list of heater positions sorted by distance from house
            closestHeater = min(heaters, key = lambda heater: abs(house - heater))
            # check if the closest heater is the worst across all houses
            if abs(house - closestHeater) > result:
                result = abs(house - closestHeater)
        
        return result
    
## Testing
      
import testOutputRev0

test = Solution()

testNo = 1

# Example 1
houses = [1,2,3]
heaters = [2]

expect = 1
output = test.findRadius(houses, heaters)
testOutputRev0.testOutput(expect, output, testNo)
testNo += 1

# Example 2
houses = [1,2,3,4]
heaters = [1,4]

expect = 1
output = test.findRadius(houses, heaters)
testOutputRev0.testOutput(expect, output, testNo)
testNo += 1
        
        