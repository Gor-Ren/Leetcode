# -*- coding: utf-8 -*-
"""
Created on Mon May 15 16:54:27 2017

@author: renn1995

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Concept: initially crawl through indices of prices in reverse. For each
        #   element, track the maximum value encountered so far and store in
        #   a dictionary of index-maximum value pairs.
        # Then, iterate up through the list. For each element, calculate the 
        #   difference between its maximum value to the right (from dict) and
        #   itself. Return the biggest difference found.
        # Assumes prices are never negative.
        
        maxPrice = 0
        bestSell = {} # dict to store best selling prices
        maxProfit = 0

        for i in reversed(range(0, len(prices))):
            # max price found to right of this element is its best selling price
            bestSell[i] = maxPrice            

            if prices[i] > maxPrice: # check for new best price
                maxPrice = prices[i]

        for i in range(0, len(prices)):
            profit = bestSell[i] - prices[i] # check the best profit for this day
            
            if profit > maxProfit:
                maxProfit = profit
                
        return maxProfit