# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:52:42 2017

@author: renn1995
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        Calculates the hamming distance between two integers, defined as the
        number of dissimilar bits in a binary representation of the two ints.
        
        :type x: int
        :type y: int
        :rtype: int
        """
        # Concept: convert each int to a binary string. Format appropriately.
        #   Crawl up shortest string and count each time characters are not
        #   equal. Add difference in length between longest and shortest string
        #   to account for zeroes in short string.
        # Rev 0 Flaw: copes poorly with ints of dissimilar binary digits.
        
        # Define x as smaller number, y as larger; rerrange if necessary.
        x, y = min(x, y), max(x, y)
        
        # Convert x, y ints to strings. Ignore first two characters (format)
        xBin = bin(x)[2:]
        yBin = bin(y)[2:]

        # Reverse strings so we can count from left
        xBinRev = xBin[::-1]
        yBinRev = yBin[::-1]
        
        # Initialise variable to store hamming distance
        hamDist = 0
        
        # For binary digit in x (by index)
        for digit in range(len(xBinRev)):
            # If digits unequal (counting effectively from left using reversed strings)
            if xBinRev[digit] != yBinRev[digit]:
                # Add to total hamming distance
                hamDist += 1
        
        # Once digits in x exhausted, add the difference in length between y 
        #   and x, noting that as the larger number y may have extra digits
        hamDist += len(yBin) - len(xBin)
        
        return hamDist
        
        