# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:42:05 2017

@author: renn1995
"""

def generatePrimes(n):
    '''
    Generates a list of all prime numbers less than n.
    n: int
    returns: list -> int
    '''
    primes = []
    
    # start testing numbers from 2 (N.B. 0 and 1 are not primes)
    num = 2
    
    while num < n:    
        for prime in primes:
            if num % prime == 0:
                # factor found, number is not a prime; break
                break
        else: # all primes exhausted, number is a prime
            primes.append(num)
        # test next num
        num += 1
    
    return primes
    
    
    