import random
from colorama import init,Fore
init(autoreset=True)
winning_combinations = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]
#display the board
def display_board(board):
    print()
    for i in range (9):
        if board[i]=="X":
            print(Fore.MAGENTA+board[i],end="")
        elif board[i]=="0":
            print (Fore.BLUE+board[i],end="")
        else:
            print(Fore.YELLOW+board[i],end="")
        #board boundaries
        if i%3!=2:
            print(Fore.CYAN+"|",end="")
        elif i!=8:
            print("\n"+Fore.CYAN+"----+----+----")
    print("\n")
#make the user able to choose a symbol
def player_choice():
    while True:
        choice = input(Fore.GREEN+"Select X or O").upper()
        if choice in ["X","O"]:
            return choice, "O" if choice == "X" else "X"
#Player move
def player_move(board,symbol):
    while True:
        move=input(Fore.GREEN+"Enter your position(1-9):")
        if move.isdigit(): #isdigit is used to convert things to digits
            move=int(move)-1
            if 0<= move <=8 and board[move] not in["X","O"]:
                board[move]=symbol
                break
            print(Fore.RED+"Invalid Move")
#ai move
def ai_move(board,ai_symbol):
    empty=[i for i in range(9) if board[i] not in ["X","O"]]
    board[random.choice(empty)]=ai_symbol
#check for the winner
def check_winner(board,symbol):
    for a,b,c in winning_combinations:
        if board[a]==board[b]==board[c]==symbol:
            return True
    return False
def check_board_full(board):
    for cell in board:
        if cell not in ["X","O"]:
            return False
    return True
#main loop(used when there are many functions in a program)
def main():
    print(Fore.YELLOW+"Welcome to tic tac toe game")
    board=["1","2","3","4","5","6","7","8","9"]
    player_symbol,ai_symbol = player_choice()
    turn="Player"
    while True:
        display_board(board)
        if turn=="Player":
            player_move(board,player_symbol)
            if check_winner(board,player_symbol):
                display_board(board)
                print(Fore.GREEN+"Player Wins")
                break
            if check_board_full(board):
                display_board(board)
                print(Fore.YELLOW+"Its a Draw")
                break
            turn="Ai"
        else:
            ai_move(board,ai_symbol)
            if check_winner(board,ai_symbol):
                display_board(board)
                print(Fore.MAGENTA+"Ai Wins")
                break
            if check_board_full(board):
                display_board(board)
                print(Fore.YELLOW+"Its a Draw")
                break
            turn="Player"
if __name__=="__main__":
    main()