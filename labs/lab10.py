#
# life.py - Game of Life lab
#
# Name: Isabella Stone
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

def testCreateBoard():
    assert createBoard(5, 3)==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

import sys

def printBoard(A):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    '''returns a 2d array of all live cells - with the value of 1
    - except for a one-cell-wide border of empty cells (with the
    value of 0) around the edge of the 2d array.'''
    A = createBoard(w, h)

    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(w,h):
    '''which returns an array of randomly-assigned 1's
    and 0's except that the outer edge of the array is still
    completely empty (all 0's) as in the case ofinnerCells.'''
    A = createBoard(w, h)

    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1]) 
    return A

def copy(A):
    '''makes a deep copy of the 2d array A. Thus, copy will take in a 2d
    array A and it will output a new 2d array of data that has the same
    pattern as the input array.'''
    new = createBoard(len(A[0]), len(A))
    return new

def innerReverse(A):
    '''that takes an old 2d array (or "generation") and then
    creates a new generation of the same shape and size (either with
    copy, above, or createBoard).'''
    
    newA = copy(A)
    w = len(newA[0])
    h = len(newA)
    
    for row in range(h):
        for col in range(w):
            if row==0 or col==0 or row==h-1 or col==w-1:
                newA[row][col] = 0
            else:
                if A[row][col]==0:
                    newA[row][col]=1
                else: #if its a 1
                    newA[row][col] = 0
    return newA

def countNeighbors(row,col,A):
    '''returns the number of live neighbors for a cell
    in the board A at a particular row and col.'''
    num = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r==row and c==col:
                pass
            elif A[r][c]==1:
                num+=1
    return num

def next_life_generation(A):
    '''d take in a 2d array A, representing the "old" generation of
    cells, and it should output the next generation of cells, each either
    0 or 1, based on John Conway's rules for the Game of Life'''
    newA = copy(A)
    w = len(A[0])
    h = len(A)

    for row in range(h):
        for col in range(w): 
            if row==0 or col==0 or row==h-1 or col==w-1: #keep edges 0
                newA[row][col] = 0
            elif countNeighbors(row, col, A)<2 or countNeighbors(row, col, A)>3:
                newA[row][col]=0
            elif A[row][col]==0 and countNeighbors(row, col, A)==3:
                newA[row][col]= 1
            else:
                newA[row][col]=A[row][col]
                
    return newA
























    

