'''
Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import *

def knapsack(capacity, itemList):
    '''returns the maximum value and the list of items that make this value, without
    exceeding the capacity of your knapsack, assuming capacity is a number and itemList
    is a list of lists that contain item weights with their values
    '''
    if itemList==[] or capacity==0: # if either var is empty
        return [0, []]
    elif itemList[0][0] > capacity: # if the weight is above the capacity, don't use it
        return knapsack(capacity, itemList[1:])
    else:
        lose = knapsack(capacity, itemList[1:])
        use = knapsack(capacity-itemList[0][0], itemList[1:])
        useList = [itemList[0][1] + use[0], [itemList[0]] + use[1]]
    if useList[0] > lose[0]:
        return useList
    else:
        return lose

