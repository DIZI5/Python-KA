import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 17)

def check_winner(board, player):
    for i in range(5):
        if all([board[i][j] == player for j in range(5)]) or \
           all([board[j][i] == player for j in range(5)]):
            return True
    if all([board[i][i] == player for i in range(5)]) or \
       all([board[i][4 - i] == player for i in range(5)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def bot_move(board):
    empty_cells = [(i, j) for i in range(5) for j in range(5) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(5)] for _ in range(5)]
    players = ["\033[32mX\033[0m", "\033[36mO\033[0m"]
    current_player = 0

    while True:
        print_board(board)
        
        if current_player == 0:
            row, col = bot_move(board)
        else:
            row = int(input(f"Player {players[current_player]}, enter row (0-4) --> "))
            col = int(input(f"Player {players[current_player]}, enter column (0-4) --> "))
        
        if board[row][col] == " ":
            board[row][col] = players[current_player]
        else:
            print("\033[31mCell is already occupied. Try again.\033[0m")
            continue
        
        if check_winner(board, players[current_player]):
            print_board(board)
            if current_player == 0:
                print("Bot wins!")
            else:
                print(f"\033[34mPlayer {players[current_player]} wins!\033[0m")
            break
        elif is_board_full(board):
            print_board(board)
            print("\033[33mIt's a draw!\033[0m")
            break
        
        current_player = 1 - current_player
    
    play_again = input("Do you want to play again? (\033[32myes\033[0m/\033[31mno\033[0m) --> ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("\033[33mThanks for playing!\033[0m")

play_game()