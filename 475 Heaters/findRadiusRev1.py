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
        # Strategy: Sort the heaters by their position. For each house, find
        #   the closest heater using an efficient search. The maximum distance
        #   to the closest heater across all houses is the required radius.
                  
        result = 0
        
        sortedHeaters = sorted(heaters)
        
        from bisect import bisect
        
        for house in houses:
            # find the insertion index of house into the sorted heater list
            i = bisect(sortedHeaters, house)
            if i == 0:
                # house must have position lower than all heaters
                closeRadius = sortedHeaters[0] - house
            elif i == len(sortedHeaters):
                # house must have position higher than all heaters
                closeRadius = house - sortedHeaters[-1]
            else:
                # else, house is somewhere in the middle of heater positions
                lower = house - sortedHeaters[i-1]
                upper = sortedHeaters[i] - house
                # find whether the left or right heater is closer
                closeRadius = min(lower, upper)
                
            # if the closest heater is higher than for any other heaters, store
            #   new result.
            if closeRadius > result:
                result = closeRadius
        
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
        
# Example 3
houses = [1,8,9,15]
heaters = [3,9]

expect = 6
output = test.findRadius(houses, heaters)
testOutputRev0.testOutput(expect, output, testNo)
testNo += 1