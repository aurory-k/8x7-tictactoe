from graphics import *
from squares import *

def checkConnection(four, box):
    checks1 = 0
    checks2 = 0

    # Checks the list of four sqaures to see if there is a connection of four
    # Consecutive checkers
    for i in range(len(four)):
        if four[i].checker==1:
            checks1+=1
        elif four[i].checker==2:
            checks2+=1

    if(checks1>=4):
        return 1
    elif checks2>=4:
        return 2
    else:
        return 0
    four = []
   
def checkAllConditions(grid, box):

    # Took me too long to figure this out... Okay
    # Decided to take the entry into lists of four at a time, because there is no
    # need to take in more or less, 4 decids the winner

    # Finds the first instance of a checker on the board and does these four
    # tests to determine winner

    # Test 1
    # Find first checker, increment each square to the right once, continue until
    # four squares have been incremented
    # Append each square to list to be checked for connection

    # Test 2
    # Same as 1, except vertical by checking up, not down

    # Test 3
    # Same as 2 and 1, except to up-right

    # Test 4
    # Same as 3, 2, and 1, except to up-left
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            
                four = []
                if(grid[r][c].checker>0):
                    # check horizontal
                    for l in range(0,4):
                        if l+r>len(grid)-1:
                            break
                        else:
                            four.append(grid[r+l][c])
                    if checkConnection(four, box)==1:
                        return 1
                    elif checkConnection(four, box)==2:
                        return 2

                    # Reset list to not get duplicates, check vertical
                    four = []
                    for col in range(0,4):
                        if c+col>6:
                            break
                        else:
                            four.append(grid[r][c+col])
                    if checkConnection(four, box)==1:
                        return 1
                    elif checkConnection(four, box)==2:
                        return 2
                    

                    # Reset list to not get duplicates, check up-right diag
                    four = []
                    for diag in range(0,4):
                        if c+diag>len(grid[0])-1 or r+diag>len(grid)-1:
                            break
                        else:
                            four.append(grid[r+diag][c+diag])
                    if checkConnection(four, box)==1:
                        return 1
                    elif checkConnection(four, box)==2:
                        return 2

                    # Reset list to not get duplicates, check up-left diag
                    four = []
                    for diag in range(0,4):
                        if c+diag>len(grid[0])-1 or r-diag<0:
                            break
                        else:
                            four.append(grid[r-diag][c+diag])
                    if checkConnection(four, box)==1:
                        return 1
                    elif checkConnection(four, box)==2:
                        return 2
                    
                
                
                

def drawCross(square, box):
    cross1 = Line(square.cross1, square.cross2)
    cross2 = Line(square.cross3, square.cross4)

    cross1.draw(box)
    cross2.draw(box)

def drawCircle(square, box):
    circle = Circle(square.mid, square.circleRadius)
    circle.draw(box)

def drawGrid(box):

    # Two separate Lists
    # One contains the entire map of squares
    # One is the entry for each row of squares
    squareList = []
    entry = []

    for col in range(8):
        # Set entry to an empty list to avoid duplicates
        entry=[]
        for row in range(7):
            # Since each square is 50 pixels wide and tall, increment by 50*the position
            rect = make_square(50*col,50*row, 50*(col+1),50*(row+1))
            shape = Rectangle(rect.a, rect.b)

            # Check to see if the column is even and row isn't and vice versa to get
            # the checkered pattern
            if(col%2==0 and row%2!=0) or (col%2!=0 and row%2==0):
                shape.setFill('brown')
            else:
                shape.setFill('red')

            entry.append(rect)
            shape.draw(box)
    
        squareList.append(entry)
        
    return squareList

def condition(square, mouse):
    # Check to see if it is within the x boundaries and y boundaries of the square
    if ((mouse.x > square.x1 and mouse.x < square.x2) and (mouse.y > square.y1 and mouse.y < square.y2)) and square.checker==0:
        return True
    
def displayNextMove(player, box):
    string = str("Next move: Player %0.0f" %player)
    label = Text(Point(20, 480), string)
    label.setSize(15)
    label.draw(box)

def displayNoOfMoves(moves, box):
    string = str("Number of Total Moves: %0.0f" %moves)
    label = Text(Point(350, 480), string)
    label.setSize(15)
    label.draw(box)

# This function should return the winner to the game function. 
def play(box, grid):
    # Make Player 1 always start first
    player = 1
    moves = 0
    while True:
        mouse = box.getMouse()
        for r in range(len(grid)):
                for c in range(len(grid[0])):
                    # Check for click within a specific square
                    if condition(grid[r][c],mouse)==True:
                        # Check to see if player 1 or player 2 clicked
                        # Draw matching 'checker' on square and change checker value
                        if player==1:
                            drawCross(grid[r][c],box)
                            grid[r][c].checker=1
                            player=2
                        elif player==2:
                            drawCircle(grid[r][c],box)
                            grid[r][c].checker=2
                            player=1          
                        moves+=1
                        # Clear top portion of screen to update moves and player
                        rect = Rectangle(Point(-100, 500), Point(510,400))
                        rect.setFill('blue')
                        rect.draw(box)
                        displayNoOfMoves(moves, box)
                        displayNextMove(player, box)
                # Checks the return value
                if checkAllConditions(grid,box)==1:
                    return 1
                elif checkAllConditions(grid,box)==2:
                    return 2
                elif moves==56:
                    return 0
                    
                            
            
   

def game():
    win = GraphWin('Tic-Tac-Toe',500,600)
    win.setBackground('blue')
    yMax = 500
    xMax = 500
    win.setCoords(-100,-150,xMax,yMax)
    grid = drawGrid(win)

    winner = play(win, grid)

    # Check winning condition
    if winner==1 or winner==2 or winner==0:
        # Clear Screen by drawing a blank blue rectangle
        rect = Rectangle(Point(-100,-300), Point(700,800))
        time.sleep(1)
        rect.setFill('blue')
        rect.draw(win)
        if winner==1:
            string = str("Player 1 Wins!")
        elif winner==2:
            string = str("Player 2 Wins!")
        else:
            string = str("Tie!")
        label = Text(Point(200, 350), string)
        label.setSize(30)
        label.draw(win)

        temp = make_square(50,150, 350,250)
        button = Rectangle(temp.a, temp.b)
        button.setFill('red')
        button.draw(win)

        string = str("Play Again?")
        label = Text(Point(200, 200), string)
        label.setSize(25)
        label.draw(win)

        mouse = win.getMouse()

        if condition(temp, mouse)==True:
            win.close()
            Main()
        else:
            win.close()
        
    

          
def Main():
    game()
if __name__ == '__main__':
    Main()
