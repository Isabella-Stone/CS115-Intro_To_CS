'''
Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import *

def numToBaseB(N, B):
    ''' takes as input a non-negative (0 or larger) integer N and a base B
    (between 2 and 10 inclusive) and returns a string representing the number
    N in base B.'''
    if N==0:
        return '0'
    else:
        return str(int(numToBaseB(N//B, B) + str(N%B)))
    
def testNumToBaseB():
    assert numToBaseB(4,2)=='100'
    assert numToBaseB(4,3)=='11'
    assert numToBaseB(4,4)=='10'
    assert numToBaseB(0,4)=='0'
    assert numToBaseB(0,2)=='0'

def baseBToNum(S, B):
    '''returns an integer in base 10 representing the same number as S; takes
    as input a string S and a base B where S represents a number in
    base B where B is between 2 and 10 inclusive'''
    if S=='':
        return 0
    else:
        return baseBToNum(S[:-1], B) * B+int(S[-1])

def testBaseBToNum():
    assert baseBToNum('11', 2)==3
    assert baseBToNum('11', 3)==4
    assert baseBToNum('11', 10)==11
    assert baseBToNum('', 10)==0

def baseToBase(B1,B2,SinB1):
    '''return a string representing the same number in base B2; takes three
    inputs: a base B1, a base B2 (both of which are between 2 and 10, inclusive)
    and SinB1, which is a string representing a number in base B1'''
    dec = baseBToNum(SinB1, B1) #converts SinB1 to decimal
    newBase = numToBaseB(dec, B2) #converts decimal to B2
    return str(newBase)

def testBaseToBase():
    assert baseToBase(2, 10, '11')=='3'
    assert baseToBase(10, 2, '3')=='11'
    assert baseToBase(3, 5, '11')=='4'
    
def add(S, T):
    '''returns the binary sum of S and T, assuming S and T are binary strings'''
    S = baseBToNum(S, 2)
    T = baseBToNum(T, 2)
    dec = S+T
    return numToBaseB(dec, 2)

def testAdd():
    assert add('11', '01')=='100'
    assert add('011', '100')=='111'
    assert add('110', '011')=='1001'

FullAdder = {
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def addB(S, T):
    '''returns the binary sum of S and T, assuming S and T are binary strings,
    accounting for if S and T are different lengths'''
    def helper(S, T, carry):
        '''helps addB by accounting for the carry value with a parameter'''
        if S=='' and T =='': #if both are empty
            if carry!='0': #if carry is not 0, return it
                return carry 
            else:
                return ''
        elif S=='': #if S is empty
            (a,w) = FullAdder[('0', T[-1], carry)]
            return helper(S, T[:-1], w) + a
        elif T=='': #if T is empty
            (a, w) = FullAdder[(S[-1], '0', carry)]
            return helper(S[:-1], T, w) + a
        else:
            (a,w) = FullAdder[(S[-1], T[-1], carry)] #r->l, so -1 to get r value
            return helper(S[:-1], T[:-1], w) + a
    return helper(S, T, '0')

def testAddB():
    assert addB('11', '1')=='100'
    assert addB('011', '100')=='111'
