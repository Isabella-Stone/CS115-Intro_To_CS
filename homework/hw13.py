'''
Isabella Stone
I pledge my honor that I have abided by the Stevens Honor System.
'''

class Board(object):

    def __init__(self, width=7, height=6):
        '''constructs the Board object (width, height, and the board itself)'''
        self.width = width
        self.height = height

        def createOneRow(width):
            '''Returns one row of zeros of width "width"...'''
            row = []
            for col in range(width):
                row += ' '
            return row

        def createBoard(width, height):
            '''returns a 2d array with "height" rows and "width" cols'''
            A = []
            for row in range(height):
                A += [createOneRow(width)]
            return A
        
        self.board = createBoard(self.width, self.height)
    

    def __str__(self):
        '''returns a string for printing the board'''
        newBoard = ''
        
        for row in range(self.height):
            for col in range(self.width):
                newBoard += ('|' + self.board[row][col])
                
                #if at last column, go to new line
                if col == self.width-1:
                    newBoard += '|\n'
        
        newBoard += ('-'*(self.width*2 + 1) + '\n ')
            
        for num in range(self.width):
            newBoard += (str(num) + ' ')

        return newBoard

        
    def allowsMove(self, col):
        '''returns True if col can have an xo moved into it'''
        #if col isn't valid return false
        if col not in range(self.width):
            return False

        full = 0
        #if col is full return False
        for r in range(self.height):
            for c in range(self.width):
                if c == col:
                    if self.board[r][c] != ' ':
                        full += 1
        if full > self.height or full == self.height:
            return False

        return True

    def addMove(self, col, ox):
        '''adds xo to the col column on the board'''
        for r in range(self.height):
                for c in range(self.width):
                    if c == col:
                        #if at bottom of col:
                        #print('1')
                        if r == self.height-1 and self.board[r][c] == ' ':
                            row = r
                            
                        #if this spot is empty but the one below it is not
                        elif self.board[r][c] == ' ' and self.board[r+1][c] != ' ':
                            row = r

        self.board[row][col] = ox

    def setBoard(self, moveString):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'

        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'


    def delMove(self,col):
        '''deletes the last move made in column col'''
        for r in range(self.height):
            if self.board[r][col] != ' ':
                self.board[r][col] = ' '
                break


    def winsFor(self, ox):
        '''checks if the ox checker has won the game,
        either horizontally, vertically, or diagnonaly'''
        count = 0

        #check hor
        #print('1')
        for r in range(self.height):
            for c in range(self.width):
                if self.board[r][c]==ox:
                    count += 1
                    if count >= 4:
                        #print(count)
                        return True
                else:
                    count = 0
            #set count back to 0 at the end of each row
            count = 0


        #check ver
        #print('2')
        for r in range(self.height-3):
            for c in range(self.width):
                if self.board[r][c]==ox:
                    if self.board[r+1][c]==ox and self.board[r+2][c]==ox and self.board[r+3][c]==ox:
                        return True
                else:
                    count = 0
    

        #check diag /
        #print('3')
        for r in range(self.height-3):
            for c in range(self.width):
                #print(r, c)
                if self.board[r][c]==ox:
                    if self.board[r+1][c-1]==ox and self.board[r+2][c-2]==ox and self.board[r+3][c-3]==ox:
                        return True
                
        
        #check other diag \
        #print('4')
        for r in range(self.height-3):
            for c in range(self.width-3):
                if self.board[r][c]==ox:
                    if self.board[r+1][c+1]==ox and self.board[r+2][c+2]==ox and self.board[r+3][c+3]==ox:
                        return True


    def hostGame(self):
        '''commands that allow players to actually play the game'''
        print('\nWelcome to Connect Four!\n')
        print(self, '\n')

        while True:
            xChoice = int(input('X\'s choice: '))
            while self.allowsMove(xChoice)==False:
                print('\nPlease enter a valid column.\n')
                xChoice = int(input('X\'s choice: '))
            print('\n')
            self.addMove(xChoice, 'x')
            if self.winsFor('x'):
                print('X wins -- Congratulations!\n')
                break
            print(self, '\n')

            oChoice = int(input('O\'s choice: '))
            while self.allowsMove(oChoice)==False:
                print('\nPlease enter a valid column.\n')
                oChoice = int(input('O\'s choice: '))
            print('\n')
            self.addMove(oChoice, 'o')
            if self.winsFor('o'):
                print('O wins -- Congratulations!\n')
                break
            print(self, '\n')

        #print(str(self))
        print(self)


'''
#for testing
A=Board(7,5)
A.board[1][0]='o'
A.board[2][0]='x'
A.board[3][0]='x'
A.board[4][0]='x'
A.board[2][1]='o'
A.board[2][2]='x'
A.board[2][3]='o'
A.board[2][4]='o'
A.board[2][5]='o'
A.board[2][6]='o'

#\
A.board[1][2]='x'
A.board[3][4]='o'
A.board[4][5]='o'

A.board[3][1]='x'
A.board[1][3]='x'
print(str(A))
'''
