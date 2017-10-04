# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:02:56 2017

@author: renn1995
"""

class Solution(object):
    def reverseWords(self, s):
        """
        Takes a string containing words separated by spaces. Outputs string
        with each word reversed but word order and spacing preserved.
        
        :type s: str
        :rtype: str
        """
        # Concept: separate input string into list of words by separating at
        #   spaces. Reverse each word in list. Create output string from list,
        #   re-attaching words with spaces.
        # Rev 1: simplifies code by using list comprehension for reverse.
        
        # Separate input string into list of words, separated by spaces
        #   (default .split delimiter)
        wordList = s.split()
        
        # For each word in list, reverse it
        reverseWordList = [word[::-1] for word in wordList]
        
        # Return string of reversed words
        return ' '.join(reverseWordList)