def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the game.
    Returns True if a player has won; otherwise, False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Runs the Tic Tac Toe game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:  # Cambiado para manejar el empate.
        print_board(board)
        
        # Validación mínima para entrada de fila
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2]:
                print("Row must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value for the row.")
            continue

        # Validación mínima para entrada de columna
        try:
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if col not in [0, 1, 2]:
                print("Column must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value for the column.")
            continue

        # Comprobación del espacio seleccionado
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Realizar el movimiento
        board[row][col] = player

        # Verificar ganador
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Cambiar de jugador
        player = "O" if player == "X" else "X"

        # Verificar empate
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

tic_tac_toe()
