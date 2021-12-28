'''
Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.
'''

def dot(L, K):
    '''outputs the dot product of the L and K, assuming L and K are lists of numbers'''
    if L==[] and K==[]:
        return 0.0 
    else:
        x = L[0]*K[0]
        return x + dot(L[1:],K[1:])
    
     
def explode(S):
    '''returns a list of the characters in s, assuming S is a string'''
    def myLen(str):
        '''returns the length using recursion, assuming x is a string'''
        if str == "":
            return 0
        else:
            return 1 + myLen(str[1:])
    if S=="":
        return [] 
    elif myLen(S)==1: 
        return [S[0]] 
    else:
        return [S[0]] + explode(S[1:])


def ind(e, L):
    '''returns the index at which e is first found in L, assuming e is an element and L is a list/string''' 
    if L==[] or L=="":
        return 0
    elif L[0]==e:
        return 0
    else:
        return 1 + ind(e, L[1:])
   

def removeAll(e, L):
    '''returns L with all instances of e removed, assuming e is an element and L is a list'''
    if L==[]:
        return []
    if L[0]==e:
        return removeAll(e, L[1:])
    if L=="":
        return L
    else:
        return [L[0]] + removeAll(e, L[1:])
    
def even(X):
    '''returns true if x is even, assuming x is a number'''
    if X % 2 == 0 : return True
    else: return False
  
def myFilter(f, L):
    '''returns a new list that contains all of the elements of L for which the predicate returns True, assuming f is a predicate and L is a list'''
    if L==[]:
        return []
    if f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])
    
def deepReverse(L):
    '''returns the reversal of L, assuming L is a list'''
    if L==[]:
        return []
    if L=="":
        return L
    else:
        if isinstance(L[0], list):
            return deepReverse(L[1:]) + [deepReverse(L[0])]
        else:
            return deepReverse(L[1:]) + [L[0]]
        
    
    
