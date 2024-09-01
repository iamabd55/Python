def boardState(board):
    print("Current State of the board: \n\n")
    for i in range(0,9):
        if((i>0)and (i%3==0)):
            print("\n")
        if(board[i]==0):
            print("\t_ ",end=" ")
        if(board[i]==-1):
            print("\tX ",end=" ")
        if(board[i]==1):
            print("\tO ",end=" ")
    print("\n\n\t\t")
        
def player1Turn(board):
    pos=input("Enter X's position from [1-9]")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong Move")
        exit(0)
    board[pos-1]=-1

def player2Turn(board):
    pos=input("Enter O's position from [1-9]")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong Move")
        exit(0)
    board[pos-1]=1

def analyzeBoard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0,8):
        if(board[cb[i][0]]!=0 and 
           board[cb[i][0]]==board[cb[i][1]] and board[cb[i][0]]==board[cb[i][2]]):
            return board[cb[i][0]]
        
    return 0
def minmax(board,player):
    x=analyzeBoard(board)
    if(x!=0):
        return (x*player)
    pos=-1
    value=-2 #the lowest value other than 1>0>-1
    for i in range(0,9):
        if(board[i]==0): #only go on empty spaces
            board[i]=player
            score=-minmax(board,player * -1)
            board[i]=0
            if(score>value):
                value=score
                pos=i
    if(pos==-1):
        return 0
    return value 
    
def computerTurn(board):
    pos=-1
    value=-2 #the lowest value other than 1>0>-1
    for i in range(0,9):
        if(board[i]==0): #only go on empty spaces
            board[i]=1
            score=-minmax(board,-1)
            board[i]=0
            if(score>value):
                value=score
                pos=i

    board[pos]=1


def main():
    choice=input("Enter 1 for Single Player, 2 for Multiplayer:")
    choice=int(choice)
    board=[0,0,0,0,0,0,0,0,0]
    if(choice==1):
        print("Computer: 0 Vs. You: X")
        player=input("Enter to play 1st or 2nd:")
        player=int(player)
        for i in range(0,9):
            if(analyzeBoard(board)!=0):
                break
            if((i+player)%2==0):
                computerTurn(board)
            else:
                boardState(board)
                player1Turn(board)
    else:
        player=input("Enter to play 1st or 2nd:")
        player=int(player)
        for i in range(0,9):
            if(analyzeBoard(board)!=0):
                break
            if((i+player)%2==0):
                boardState(board) 
                player1Turn(board)
            else:
                boardState(board)
                player2Turn(board)

    x=analyzeBoard(board)
    if(x==0):
        boardState(board)
        print("Draw!")
    if(x==-1):
        boardState(board)
        print("Player X Wins!!")
    if(x==1):
        boardState(board)
        print("Player O Wins!!")
main()