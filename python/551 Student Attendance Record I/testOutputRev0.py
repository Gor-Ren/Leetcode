# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:31:44 2017

@author: renn1995
"""

def testOutput(expected, actual, testNo, testInput = 'UNKNOWN'):
    '''
    Tests whether input lists are equal, and prints test result accordingly.
    
    expected: list -> ints
    actual: list -> ints
    returns nothing.
    '''
    if expected == actual:
        print('PASS Test ' + str(testNo))
    else:
        print('FAIL Test ' + str(testNo))
        
    print('\tTest input:\t', testInput)  
    print('\tExpected output:\t', expected)
    print('\tActual output:\t\t', actual)