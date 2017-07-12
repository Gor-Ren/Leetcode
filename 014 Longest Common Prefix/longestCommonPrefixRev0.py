# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:12:27 2017

@author: renn1995
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix string from an array of strings.
        :type strs: List[str]
        :rtype: str
        """
        # Concept: iterate through character of zeroth string. Check that it
        #   matches all other strings. Add char to prefix string. Iterate to next
        #   character and repeat until match not found. Return prefix string.
        
        prefix = ''
        
        # Edge case: input list is empty. Return empty string.
        if strs == []:
            return ''
            
        # Edge case: input list contains one element. Return element.
        if len(strs) == 1:
            return strs[0]
        
        # For each character in zeroth string
        for charIndex in range(len(strs[0])):
            currentChar = strs[0][charIndex]
            # Set flag to track whether char at index is the same for all strings
            charFlag = True
            # Begin iterating to every other string in list
            for string in strs[1:]:
                try:
                    # If we have a non-match in characters at index for any string
                    if string[charIndex] != currentChar:
                        # Set flag to false and break out of loop
                        charFlag = False
                        break
                    
                # Catch any IndexErrors (indicating zeroth string is longer
                #   than any other string) and break from for loop.
                except IndexError:
                    break
            # Else (for loop exhausts iterations successfully, N.B. for-else)
            else:
                # add character to prefix string.
                prefix += currentChar
                
            # If we flagged non-match, break out of second loop as well.
            if charFlag == False:
                break
            
        # Return prefix string
        return prefix                
            
        