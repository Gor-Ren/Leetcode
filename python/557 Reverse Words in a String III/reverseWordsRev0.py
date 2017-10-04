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
        
        # Separate input string into list of words, separated by spaces
        #   (default .split delimiter)
        wordList = s.split()
        
        # Set up list for reversed words
        reverseWordList = []
        
        # For each word in list
        for word in wordList:
            # Reverse the word
            reverseWordList.append(word[::-1])

        # Return string of reversed words
        return ' '.join(reverseWordList)