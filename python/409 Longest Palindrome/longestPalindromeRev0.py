# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:45:44 2017

@author: renn1995
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        Given a string of case-sensitive characters, returns the maximum
        possible palindrome length that can be created.
        
        :type s: str
        :rtype: int
        """
        # Concept: Count all characters as keys into a dictionary. Values
        #   correspond to the occurances of that character.
        #   A palindrome is made up of symmetrically ordered pairs of letters.
        #   Therefore its length is dictated by the number of same-letter same-
        #   case pairs in the dictionary. Additionally a single odd character
        #   of any letter may be used as the palindrome central letter.
        
        # Create dictionary to store character quantities
        letterDict = {}
        
        # For each char in string
        for char in s:
            # Add 1 to that key. If it doesn't exist, create it. N.B. that
            #   dict.get returns 0 if ch is not found.
            letterDict[char] = letterDict.get(char,0) + 1

        # Create var to store length of longest palindrome
        longest = 0
        # Create var to store presence of an odd letter. Max value 1
        oddLetter = 0
        
        # Iterate through letter keys in dict
        for char in letterDict.keys():
            # Add the number of chars contained in pairs 
            longest += (letterDict[char] // 2) * 2
            # If we have an odd letter in any character
            if letterDict[char] % 2 == 1:
                # odd letter count becomes 1. Does not exceed 1.
                oddLetter = 1
                
        # Return sum of number of pairs and odd letter
        return longest + oddLetter