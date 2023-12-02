import random

def print_board(board):
    line = "+-------------------+"
    print(line)
    for i in range(4):
        row = "|"
        for j in range(4):
            cell = str(board[i][j]) if board[i][j] != 0 else " "
            row += "{:^4}|".format(cell)
        print(row)
        print(line)

def find_blank(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j

def is_valid_move(move):
    return move in ["w", "a", "s", "d"]

def make_move(board, move):
    blank_i, blank_j = find_blank(board)
    new_i, new_j = blank_i, blank_j
    
    if move == "w":
        new_i -= 1
    elif move == "a":
        new_j -= 1
    elif move == "s":
        new_i += 1
    elif move == "d":
        new_j += 1
    
    if 0 <= new_i < 4 and 0 <= new_j < 4:
        board[blank_i][blank_j], board[new_i][new_j] = board[new_i][new_j], board[blank_i][blank_j]
        return True
    return False

def is_game_over(board):
    return board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def main():
    board = [[0, 0, 0, 0] for _ in range(4)]
    
    nums = list(range(1, 16))
    random.shuffle(nums)
    
    for i in range(4):
        for j in range(4):
            if nums:
                board[i][j] = nums.pop()
    
    while not is_game_over(board):
        print_board(board)
        
        move = input("Enter move (w/a/s/d): ")
        if is_valid_move(move):
            if make_move(board, move):
                print()
            else:
                print("Invalid move! Try again.")
        else:
            print("Invalid input! Use w/a/s/d.")

    print("Congratulations! You've solved the puzzle.")

if __name__ == "__main__":
    main()