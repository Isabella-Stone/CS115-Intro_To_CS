'''
Created on October 11, 2020
@author:   Isabella Stone
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 (Rev. Oct 2020 by D.N.)
'''
import turtle  # Needed for graphics

def sv_tree(trunk_length, levels):
    '''draws a tree with levels levels and a trunk with a length trunk_length,
    assuming trunk_length and levels are positive integers'''
    turtle.pencolor("green")
    turtle.pensize(2)
    if levels>0:
        if levels>2:
            turtle.pencolor("brown")
            turtle.pensize(5)
            if levels>4:
                turtle.pensize(7)
        turtle.pendown()
        turtle.forward(trunk_length)
        turtle.left(45)
        sv_tree(trunk_length/2, levels-1)
        turtle.right(90)
        sv_tree(trunk_length/2, levels-1)
        turtle.left(45)
        turtle.forward(-trunk_length)
        turtle.penup()
    else:
        return

'''       
memo = {}
def fast_lucas(n):
    ''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]''
    if n in memo:
        return memo[n]
    if n==0:
        memo[0]=2
        return 2
    if n==1:
        memo[1]=1
        return 1
    else:
        memo[n]=fast_lucas(n-1)+fast_lucas(n-2)
        return fast_lucas(n-1)+fast_lucas(n-2)
'''

memo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in memo:
        return memo[n]
    elif n==0:
        result = 2
    elif n==1:
        result = 1
    else:
        result = fast_lucas(n-1)+fast_lucas(n-2)

    memo[n] = result
    return result


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        '''Does the job of fast_change, assuming coins is a tuple.'''
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if amount == 0:
            memo[(amount, coins)] = 0
            return 0
        elif len(coins) == 0:
            memo[(amount, coins)] = float("inf")
            return float("inf")
        elif coins[0] > amount:
            memo[(amount, coins)] = fast_change_helper(amount, coins[1:], memo)
            return fast_change_helper(amount, coins[1:], memo)
        else: # coins[0] <= amount
            lose = fast_change_helper(amount, coins[1:], memo)
            use = fast_change_helper(amount - coins[0], coins, memo) + 1
            memo [(amount, coins)] = min(use, lose)
            return min(use, lose)

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})


def fast_change2(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        '''Does the job of fast_change, assuming coins is a tuple.'''
        if (amount, coins) in memo:
            result = memo[(amount, coins)]
        if amount == 0:
            result = 0
        elif len(coins) == 0:
            result = float("inf")
        elif coins[0] > amount:
            result = fast_change_helper(amount, coins[1:], memo)
        else: # coins[0] <= amount
            lose = fast_change_helper(amount, coins[1:], memo)
            use = fast_change_helper(amount - coins[0], coins, memo) + 1
            result = min(use, lose)

        memo[(amount, coins)] = result
        return result

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})


# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change2(131, [1, 5, 10, 20, 50, 100])) #4
print(fast_change2(292, [1, 5, 10, 20, 50, 100])) #7
print(fast_change2(673, [1, 5, 10, 20, 50, 100])) #11
print(fast_change2(724, [1, 5, 10, 20, 50, 100])) #12
print(fast_change2(888, [1, 5, 10, 20, 50, 100])) #15

# Should take a few seconds to draw a tree.
# sv_tree(100, 4)
