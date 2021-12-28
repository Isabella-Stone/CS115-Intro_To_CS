'''
Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import *

def change(amount, coins):
    '''returns the minumum number of coins needed to make amount,
    assuming amount is a non-negative integer and coins is a list
    of coin values starting with 1'''
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else: # coins[0] <= amount
        lose = change(amount, coins[1:])
        use = change(amount - coins[0], coins) + 1
        return min(use, lose)


        
