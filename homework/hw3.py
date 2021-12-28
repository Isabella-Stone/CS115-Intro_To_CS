'''
Created on 9/27/20
@author:   Isabella Stone
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def giveChange(amount, coins):
    '''returns the minumum number of coins needed to make amount,
    assuming amount is a non-negative integer and coins is a list
    of coin values starting with 1'''
    if amount == 0:
        return [amount, []]
    elif coins == []:
        return (float("inf"), [])
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:#coins[0] <= amount
        lose = giveChange(amount, coins[1:])
        use = giveChange(amount - coins[0], coins)
        useList= (use[0]+1, [coins[0]] + use[1])
        if useList[0]<lose[0]:
            return useList
        else:
            return lose
        
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def explode(S) :
    '''Takes a string S as input and returns a list of the characters'''
    if S == "" or S == []:
        return []
    else:
        return [S[0]] + explode(S[1:])
    
def letterScore(letter, scorelist):
    '''returns the number associated with letter in scorelist, assuming
    letter is a single letter string and scorelist is a list where each element
    is in the form [character, value]'''
    x = scorelist[0]
    if x[0]==letter: 
        return x[1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''returns the scrabble score of S, assuming S is a string and scorelist is a list
    where each element is in the form [character, value]'''
    word = explode(S)
    if len(word)==1:
        return letterScore(word[0], scorelist) 
    else:
        return letterScore(word[0], scorelist) + wordScore(S[1:], scorelist)

   
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct==[]:
        return []
    else:
        return [[dct[0]] + [wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming n is a number and L is a list'''
    if n==0:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming n is a number and L is a list'''
    # drop(2, [1,2,3,4]) ---> [3,4]
    if L==[]:
        return []
    if n+1==len(L):
        return [L[n]]
    else:
        return [L[n]] + drop(n+1, L)


