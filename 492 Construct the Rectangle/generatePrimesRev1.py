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
    # Strategy: use fact that you only need to test has any prime number lower
    #   than its square root as a factor to determine whether it's a prime.
    # Apply memoisation: record primes as they are found and use them to calc
    #   next primes.
    #   Rev1: added statement to stop checking prime factors once you exceed
    # square root of given number.
    
    primes = []
    
    # start testing numbers from 2 (N.B. 0 and 1 are not primes)
    num = 2
    
    while num < n:
        numRoot = num ** 0.5
        isPrime = True
        
        for prime in primes:      
            if prime > numRoot:
                # we can stop testing once we have checked all primes up to sqrt
                break
            elif num % prime == 0:
                # factor found, number is not a prime; break
                isPrime = False
                break 
        
        if isPrime: # if we finish or break from for loop, check for prime
            primes.append(num)
        # test next num
        num += 1        
    
    return primes
    
    
    