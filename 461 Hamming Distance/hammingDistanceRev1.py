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
        # Rev 1: improved and simplified code by adding zero fill for shorter
        #   input value. Resolved incorrect output when x, y are binary no.s
        #   of different lengths.
        
        # Define x as smaller number, y as larger; rearrange if necessary.
        x, y = min(x, y), max(x, y)
        
        # Convert x, y ints to strings. Ignore first two characters (format)
        xBin = bin(x)[2:]
        yBin = bin(y)[2:]

        # Pad x (smallest value) with zeroes if it is a different length than y
        xBin = xBin.zfill(len(yBin))
        
        # Initialise variable to store hamming distance
        hamDist = 0
        
        # For binary digit in x (by index)
        for digit in range(len(xBin)):
            # If digits unequal
            if xBin[digit] != yBin[digit]:
                # Add to total hamming distance
                hamDist += 1
        
        return hamDist
        
        