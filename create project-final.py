board=[[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]
turn = 1
#1 is black, -1 is white, and 0 is an empty space

    
board_size = len(board)
win_number = 4

def printboard():
    output = "  0 1 2 3 4 5 6 7 \n"
    for i in range(board_size):
        output += str(i)+ " "
        for j in range(board_size):
            if board[i][j] == 1:
                output += "b "
            elif board[i][j] == -1:
                output += "w "
            elif board[i][j] == 0:
                output += "- "
        output += "\n"
    print(output)

def move(x,y):
    global turn
    if board[x][y]==0:
        #player can make a move
        board[x][y]= turn
        turn *= -1
        return True
    else:
        #player cannot make a move
        print ("Not a valid move")
        return False

#a function that checks for a four in a row
def check_win(x,y):
    count_up = 0
    count_down = 0
    count_right = 0
    count_left = 0
    count_ur = 0
    count_ul = 0
    count_dr = 0
    count_dl = 0
    lastmove = board[x][y]
    if lastmove == 0:
        return False
    for i in range(1, win_number):
        if x-i >= 0 and board[x-i][y] == lastmove:
            count_up += 1
        else:
            break    
    for i in range(1, win_number):
        if x+i < board_size and board[x+i][y] == lastmove:
            count_down += 1
        else:
            break    
    for i in range(1, win_number):
        if y+i < board_size and board[x][y+i] == lastmove:
            count_right += 1
        else:
            break    
    for i in range(1, win_number):
        if y-i >= 0 and board[x][y-i] == lastmove:
            count_left += 1
        else:
            break 
    for i in range(1, win_number):
        if y+i < board_size and x+i < board_size and board[x+i][y+i] == lastmove:
            count_dr += 1
        else:
            break 
    for i in range(1, win_number):
        if x-i >= 0 and y+i < board_size and board[x-i][y+i] == lastmove:
            count_ur += 1
        else:
            break
    for i in range(1, win_number):
        if x+i < board_size and  y-i >= 0 and board[x+i][y-i] == lastmove:
            count_dl += 1
        else:
            break
    for i in range(1, win_number):
        if x-i >= 0 and y-i >= 0 and board[x-i][y-i] == lastmove:
            count_ul += 1
        else:
            break
    if count_up + count_down >= win_number - 1 or count_right + count_left >= win_number - 1 or count_ur + count_dl >= win_number - 1 or count_ul + count_dr >= win_number - 1:
        return True
    else:
        return False
    


while True:
    x=0
    y=0
    #starts with an empty board in the beginning
    #the player who lost will start first
    board=[[0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]
    print("Let's play four in a row!!")
    print("Instructions:\n1. Type coordinate where you want to make a move (row + space + column + enter)\n2. 'b' denotes black and 'w' denotes white")
    print("3. The player who has 4 pieces of the same color in a row horizontally, vertically or diagonally wins.")
    printboard()
    while check_win(x,y) is False:
        if turn == 1:
            player = "Black"
        elif turn == -1:
            player = "White"
        #handling errors caused by user
        while True:
            try:
                pos=input(player+" to move ")
                pos=pos.split()
                x=int(pos[0])
                y=int(pos[1])
                board[x][y]
                break
            except:
                print("Wrong input\nType coordinate where you want to make a move (row + space + column + enter)")
        move(x,y)
        printboard()
    print("Game Over")
    if turn == -1:
        winner = "Black"
    elif turn == 1:
        winner = "White"
    print(winner + " wins!!")
    restart=input("Restart? (type yes to restart and no to stop) ")
    if restart == "no":
        print("Well done")
        break

            






