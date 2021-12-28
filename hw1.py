'''Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.'''


from cs115 import *

def mult(x, y):
 '''Returns the product of x and y, assuming they are numbers'''
 return x * y

def factorial(n):
        '''returns the factorial of n, assuming n is a positive integer'''
        return reduce(mult, range(1,n+1))

def mean(L):
    '''returns the average of L, assuming L is a list of numbers'''
    def add(x,y):
        '''returns the sum of x&y, assuming they are numbers'''
        return x+y
    return reduce(add,L)/len(L)

def divides(n):
    '''returns div, assuming n is a number'''
    def div(k):
        '''returns a boolean (true if n is divisible by k), assuming k is an integer'''
        return n % k == 0
    return div

def prime(n):
    '''returns a boolean (true if n is prime), assuming n is a positive integer'''
    lst = range(1, n)
    lst2 = map(divides(n), lst)
    return sum(lst2) <= 1

