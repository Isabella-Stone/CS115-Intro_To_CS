# mandelbrot.py
# Lab 9
#
# Name: Isabella Stone
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c, n):
     '''mult uses only a loop and addition
     to multiply c by the integer n'''
     result = 0
     for x in range(n):
         result += c
     return result

def testMult():
    assert (mult(0, 7)==0)
    assert (mult(8, 0)==0)
    assert (mult(2, 3)==6)
    assert (mult(1, 7)==7)
    assert (mult(9, 1)==9)
    assert (mult(6, 7)==42)
    assert (mult(1.5, 28)==42.0)

def update(c, n):
     '''update starts with z=0 and runs z = z**2 + c
     for a total of n times. It returns the final z.'''
     z = 0
     for x in range(n):
          z = z**2 + c
     return z

def testUpdate():
     assert (update(1, 3)==5)
     assert (update(-1, 3)==-1)
     assert (update(1, 10)==3791862310265926082868235028027893277370233152247388584761734150717768254410341175325352026)
     assert (update(-1, 10)==0)

###############################################################

def inMSet(c, n):
     '''inMSet takes in c for the update step of z = z**2+c
     n, the maximum number of times to run that step.
     Then, it should return False as soon as abs(z) gets larger than 2,
     True if abs(z) never gets larger than 2 (for n iterations)'''
     z = 0
     for x in range(n):
          z = z**2 + c
          if abs(z)>2:
               return False
     #if loop never returns False return True:
     return True

def testInMSet():
     assert (inMSet((0+0j), 25)==True)
     assert (inMSet((3+4j), 25)==False)
     assert (inMSet((.3-.5j), 25)==True)
     assert (inMSet((-.7+.3j), 25)==False)
     assert (inMSet((.42+.2j), 25)==True)
     assert (inMSet((.42+.2j), 50)==False)
















     
