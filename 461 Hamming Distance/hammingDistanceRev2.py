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
        # Rev 2 Concept: Use bitwise XOR (^) on input ints to get a binary
        #   number where 1s correspond to differences between the binary
        #   representations of x and y. Sum the 1s and output.
        
        # Apply bitwise XOR
        hamDistBin = bin(x ^ y)
        
        # Count 1s to find hamming distance
        hamDist = hamDistBin.count('1')
        
        return hamDist
        
        