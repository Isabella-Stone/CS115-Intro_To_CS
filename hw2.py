'''
Isabella Stone and Matthew Hullstrung
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import *

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1],
["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1],
["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1],
["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

def letterScore(letter, scorelist):
    '''returns the number associated with letter in scorelist, assuming
    letter is a single letter string and scorelist is a list where each element
    is in the form [character, value]'''
    x = scorelist[0]
    if x[0]==letter: 
        return x[1]
    else:
        return letterScore(letter, scorelist[1:])

def explode(S) :
    '''Takes a string S as input and returns a list of the characters'''
    if S == "" or S == []:
        return []
    else:
        return [S[0]] + explode(S[1:])
    
def wordScore(S, scorelist):
    '''returns the scrabble score of S, assuming S is a string and scorelist is a list
    where each element is in the form [character, value]'''
    word = explode(S)
    if len(word)==1:
        return letterScore(word[0], scorelist) 
    else:
        return letterScore(word[0], scorelist) + wordScore(S[1:], scorelist)

Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo",
"spam","spammy", "zzyzva"]

def remove(L):
    '''returns a list identical to L but removes the first appearance of global character c'''
    if L == "":
        return ""
    elif L[0] == c:
        return "" + L[1:]
    else:
        return L[0] + remove(L[1:])
    
def ind(e, L): 
    '''Takes in an element e and a sequence L ( a list or string) and returns the index at which e is first found in L'''
    if L == []:
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])

c = ''
d = Dictionary
num = 0
def removeFromList(Rack) :
    '''Removes the first occurance of each character in the list Rack from global list d'''
    if Rack == []:
        return []
    global c
    global d
    c = Rack[0]     #c is recursively set to each Rack character
    d = map(remove,d)   #here, we remove the first occurance of c in every element of global list d
    return removeFromList(Rack[1:])
    

def wordList():
    '''By finding the indeces of where all characters were removed from an element in d, we will 
    search the dictionary for this index to find the word that contained strictly letters from Rack'''
    global d
    global num
    if not (ind('', d) == len(d)):
        x = ind('', d)   #index of word containing letters strictly from Rack
        d.remove('')     #removes where this word was in order to find the next, if there is one
        num += 1  #counter
        word = Dictionary[x + num - 1]
        return [[word, wordScore(word, scrabbleScores)]] + wordList()  #returns the word with its score then recurses
    else:
        return []

def reset():
    '''resets global variables back to initial states'''
    global c
    global d
    global num
    c = ''
    d = Dictionary
    num = 0

def scoreList(Rack):
    '''returns a list of the words that can be made with Rack and their scores,
    assuming Rack is a list of all lowercase letters.'''
    reset()
    removeFromList(Rack)
    if wordList() == []:
        return ['', 0]
    reset()
    removeFromList(Rack)
    return wordList()


def bestWord(Rack):
    '''returns a list with 2 elements: the highest possible scoring word from that
    Rack followed by its score, assuming Rack is a list of all lowercase letters.'''
    if scoreList(Rack) == ['', 0]:
        return ['', 0]
    def max(x,y):
        if x[1] > y[1]:
            return x
        else:
            return y
    return reduce(max,scoreList(Rack))


