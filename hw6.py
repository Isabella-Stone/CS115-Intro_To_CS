'''
Created on October 15, 2020
@author:   Isabella Stone
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''

from cs115 import *

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2!=0

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

def repeatLen(S):
    '''returns the number of times the first digit repeats,
    assuming S is a string'''
    if len(S)==1:
        return 1
    elif S[0]!=S[1]:
        return 1
    else:
        return 1 + repeatLen(S[1:])

def fix(S):
    '''makes sure S is 5 bits, assuming S is a binary string'''
    return '0'*(COMPRESSED_BLOCK_SIZE-len(str(S))) + S
    
def compress(S):
    '''returns the binary runlength of S, assuming S is a binary string'''
    def helper(S):
        '''returns a runlength list of S in decimal values,
        assuming S is a binary string'''
        #helps make decList
        if S=='':
            return []
        else:
            return [repeatLen(S)] + helper(S[repeatLen(S):])
    if S[0]!='0': # add 0 to front of list if S didn't start w 0's
        decList = [0] + helper(S)
    else:
        decList = helper(S)
    #before turning dec-->bin, account for 5 bits, so if>31 need to fix it
    def adjust(lst):
        if lst==[]:
            return []
        if lst[0]>31:
            lst[0] = lst[0] - 31
            return [31, 0] + adjust(lst)
        else: #if <=31
            return [lst[0]] + adjust(lst[1:])
    decList = adjust(decList)
    #convert decList to binary:
    binList = map(numToBinary, decList)
    fixedBinList = map(fix, binList)
    #combine to single string:
    def add(x, y):
        return x+y
    finalList = reduce(add, fixedBinList)
    return finalList

def uncompress(C):
    '''undoes the compression of C, assuming C is the binary
    runlength of a binary string'''
    def helper(C):
        '''
        returns a list of every 5 bits of C converted to a decimal value,
        assuming C is a binary string
        '''
        if C=='':
            return []
        else:
            return [binaryToNum(C[0:5])] + helper(C[5:])
    binList = helper(C)
    def helper2(lst, num):
        '''
        builds a binary list starting w 0 then 1 and on... where each repeats based on the
        values from lst, assuming lst is a list of decimal values and num is an integer
        '''
        if lst==[]:
            return ''
        elif num==0:
            return '0'*lst[0] + helper2(lst[1:], 1-num)
        else:
            return '1'*lst[0] + helper2(lst[1:], 1-num)
    newList = helper2(binList, 0)
    return newList
    
def compression(S):
    '''return the ratio of the compressed size to the original size for
    image S, assuming S is a binary string'''
    if len(S)==0:
        return
    else:
        return len(compress(S))/len(S)


    
