# nim template DNaumann (2018), for assignment nim_hw11.txt 
'''
Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.
'''
# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)

from cs115 import *

def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """

    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print('You win!')

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            # TODO print a message telling the user the computer won

            print('I win!!!!!!')
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    #print('init_piles')
    global piles
    global num_piles

    num_piles = int(input("How many piles do you want to play with? "))
    while num_piles<2: #get user to enter integer for num_piles
        print('Please enter an integer greater than 1.')
        num_piles = int(input("How many piles do you want to play with? "))

             
    piles = [0] * num_piles #gives piles num_piles items
    
    for i in range(num_piles): #fills piles with coins at each index
        num_per_pile = int(input('How many in pile ' + str(i) + '? '))
        while num_per_pile <1:
            print('Please enter a number 1 or higher.')
            num_per_pile = int(input('How many in pile ' + str(i) + '? '))
        piles[i] = num_per_pile
        #print(piles)

        
def display_piles():
    """ display current amount in each pile """
    #print('display_piles')
    global piles
    global num_piles

    for i in range(num_piles):
        print('pile ' , i , ' = ' , piles[i])


def user_plays(): #uses get_pile and get_number
    """ get user's choices and update chosen pile """
    #print('user_plays')
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    #print('get_pile')
    global piles
    global num_piles

    user_pile_choice = int(input("Which pile? "))
    #dont let them select a pile that doesn't exist, OR a pile that has 0 coins
    while ((user_pile_choice not in range(0, num_piles)) or (piles[user_pile_choice]==0)):
        print('Please enter a valid pile choice.')
        user_pile_choice = int(input("Which pile? "))

    return user_pile_choice
         
def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    #print('get_number')
    global piles
    
    user_remove_choice = int(input("How many? "))
    while user_remove_choice not in range(1, piles[pnum]+1):
        print('Please enter a number no greater than the amount in your chosen pile.')
        user_remove_choice = int(input("How many? "))

    return user_remove_choice


########################################################

def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 
    
    nim_sum = reduce(lambda x,y: x^y, piles)
    return nim_sum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles
    
    
    pile_sums_list = [0] * num_piles
    #sets each item in pile_sums_list to its pile-sum
    for i in range(0, num_piles):
        pile_sums_list[i] = piles[i]^game_nim_sum()

    #if the pile_sum is less than the pile choose this one
    for i in range(0, num_piles):
        if pile_sums_list[i] < piles[i]:
            return (i, (piles[i] - pile_sums_list[i]))

    #if it never returned in the for loop^ pick 1 from the first non-empty pile
    #print('****')
    for i in range(0, num_piles):
        if piles[i]>0:
            return (i, 1)

def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played
        Implement this using opt_play(). """
    global piles
    global num_piles

    optimal_play = opt_play()
    opt_pile = optimal_play[0]
    opt_amt = optimal_play[1]

    #update piles by subtracting the proper amount from the proper pile
    piles[opt_pile] = piles[opt_pile] - opt_amt

    print('I remove', opt_amt , 'from pile' , opt_pile)

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
