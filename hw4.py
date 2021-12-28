'''
I pledge my honor that I have abided by the Stevens Honor System.
Isabella Stone
'''

from cs115 import *

def add(list):
    '''returns a list of the sum of adjacent terms in list, assuming
    list is a list of numbers'''
    if len(list)==1:
        return []
    else:
        return [list[0]+list[1]] + add(list[1:])

def pascal_row(row):
    '''returns a list of elements found in a certain row of Pascal’s Triangle
    assuming row is a number'''
    if row==0:
        return [1]
    if row==1:
        return [1] + [1]
    else:
        return [1] + add(pascal_row(row-1)) + [1]

def pascal_triangle(n):
    '''returns a list of lists containing the values of the all the rows
    up to and including row n, assuming n is an integer'''
    if n==0:
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''uses assert to test pascal_row(row)'''
    assert (pascal_row(0) == [1])
    assert (pascal_row(1) == [1,1])
    assert (pascal_row(5) == [1, 5, 10, 10, 5, 1])
    assert (pascal_row(8) == [1, 8, 28, 56, 70, 56, 28, 8, 1])
    
def test_pascal_triangle():
    '''uses assert to test pascal_triangle(n)'''
    assert (pascal_triangle(0) == [[1]])
    assert (pascal_triangle(1) ==[[1], [1, 1]])
    assert (pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    assert (pascal_triangle(7) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]])
