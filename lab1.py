#I pledge my honor that I have abided by the Stevens Honor System.
#Isabella Stone

from cs115 import *
import math 

def inverse(n):
    '''returns the reciprocal of n, assuming n is a number'''
    return 1/n

def e(n):
    '''approximates the value e using the first n terms, assuming n is a positive integer'''

    def mult(x,y):
        '''multiplies x&y, assuming they are numbers'''
        return x*y
    
    def factorial(N):
        '''assuming N is a number > or = 0'''
        return reduce(mult, range(1,N+1))

    def add(x,y):
        '''adds x&y, assuming they are numbers'''
        return x+y

    list1 = range(1, n+1) #list of integers up to n
    list2 = map(factorial, list1) #list of factorials of each num in list1 
    list3 = map(inverse, list2) #makes inverse fractions of the factorials
    return reduce(add, list3) + 1

def error(n):
    ''' returns the abs val of the difference between the "actual" value of e and the approximation of e from e(n), assuming n is a number'''
    return abs(e(n)-math.e)
