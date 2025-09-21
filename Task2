import math

# Function to check winner
def check_winner(board):
    win_patterns = [(0,1,2), (3,4,5), (6,7,8),
                    (0,3,6), (1,4,7), (2,5,8),
                    (0,4,8), (2,4,6)]
    for (x,y,z) in win_patterns:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return board[x]
    return None

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "O": return 1   # AI wins
    if winner == "X": return -1  # Human wins
    if " " not in board: return 0  # Draw

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha: break
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha: break
        return best_score

# Best move for AI
def best_move(board):
    move = -1
    best_score = -math.inf
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Print board nicely
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")
    print()

# Play the game
def play_game():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe! (You are X, AI is O)")
    print_board(board)

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        print("\nYour move:")
        print_board(board)

        if check_winner(board) == "X":
            print("🎉 You win!")
            break
        if " " not in board:
            print("It's a draw!")
            break

        # AI move
        ai_choice = best_move(board)
        board[ai_choice] = "O"
        print("AI's move:")
        print_board(board)

        if check_winner(board) == "O":
            print("🤖 AI wins!")
            break
        if " " not in board:
            print("It's a draw!")
            break

# Run game
play_game()
