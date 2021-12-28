'''
Created on October 14 2020
@author:   Isabella Stone
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2!=0

'''
42(base10) --> 101010(base2)
'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif isOdd(n): 
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'
'''
If you are given an odd base10 number, the rightmost bit in base2 will be 1,
and if you are given an even base10 number, the rightmost bit will be 0.

When eliminating the least significant bit, this divides the base10 number by 2
using integer division (rounds down).

To get from Y to N, if N is odd you add a 1 to the rightmost end of Y, and if N is even
you add a 0 to the rightmost end of Y.
'''
  
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[0]=='1':
        return binaryToNum(s[1:]) + (2**(len(s)-1))
    else: # if s[0]=='0'
        return binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s=='11111111':
        return '00000000'
    ten = binaryToNum(s) #changes to decimal
    ten+=1 #adds 1 to decimal
    new = numToBinary(ten) #changes back to binary
    if len(new)<8:
        return '0'*(8-len(new)) + new
    else:
        return new

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n==0:
        return
    else:
        count(increment(s), n-1)    

'''
The ternary representation for the value 59 is 2012.  This is so because when you add
2*(3**3), 0*(3**2), 1*(3**1), and 2*(3**0), you get 59.
'''

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n<3:
        return str(n)
    else:
        return numToTernary(n//3) + str(n%3)
    
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[0]=='1':
        return ternaryToNum(s[1:]) + (3**(len(s)-1))
    elif s[0]=='2':
        return ternaryToNum(s[1:]) + 2*(3**(len(s)-1))
    else: # if s[0]=='0'
        return ternaryToNum(s[1:])


    
