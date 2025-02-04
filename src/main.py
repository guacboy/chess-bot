chess_board_dict = {
    "a8": "black_rook", "b8": "black_knight", "c8": "black_bishop", "d8": "black_queen", "e8": "black_king", "f8": "black_bishop", "g8": "black_knight", "h8": "black_rook", 
    "a7": "black_pawn", "b7": "black_pawn", "c7": "black_pawn", "d7": "black_pawn", "e7": "black_pawn", "f7": "black_pawn", "g7": "black_pawn", "h7": "black_pawn", 
    "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None, 
    "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None, 
    "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None, 
    "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None, 
    "a2": "white_pawn", "b2": "white_pawn", "c2": "white_pawn", "d2": "white_pawn", "e2": "white_pawn", "f2": "white_pawn", "g2": "white_pawn", "h2": "white_pawn", 
    "a1": "white_rook", "b1": "white_knight", "c1": "white_bishop", "d1": "white_queen", "e1": "white_king", "f1": "white_bishop", "g1": "white_knight", "h1": "white_rook",
}
chess_piece_dict = {
    "black_king": "♚",
    "black_queen": "♛",
    "black_rook": "♜",
    "black_bishop": "♝",
    "black_knight": "♞",
    "black_pawn": "♟",
    "white_king": "♔",
    "white_queen": "♕",
    "white_rook": "♖",
    "white_bishop": "♗",
    "white_knight": "♘",
    "white_pawn": "♙",
}

def display_chess_board() -> None:
    # prints the chess board with current pieces
    chess_row = ""
    print("  +----+----+----+----+----+----+----+----+")
    for number in range(8, 0, -1): # move number notation
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h"]: # move letter notation
            # if the current space is empty
            if chess_board_dict[letter + str(number)] is None:
                # adds an empty space
                chess_row += "    |"
            # if the current space has a piece
            else:
                # adds the piece to the board
                chess_row += f" {chess_piece_dict[chess_board_dict[letter + str(number)]]}  |"
        print(f"{number} |{chess_row}")
        print("  +----+----+----+----+----+----+----+----+")
        chess_row = ""
    print("    a    b    c    d    e    f    g    h") # board letter notation

def white_to_move() -> None:
    piece_notation = ["K", "Q", "R", "B", "N"]
    letter_notation = ["a", "b", "c", "d", "e", "f", "g", "h"]
    is_valid_move = False
    while is_valid_move is False:
        next_move = input("YOUR TURN: ")
        
        next_move_notation = next_move[-2:]
        next_move_letter_notation = next_move[-2]
        next_move_number_notation = next_move[-1]
        
        # if moving a pawn
        if next_move[0] not in piece_notation:
            if chess_board_dict[next_move_notation] is None:
                
                # moves the pawn up from inital placement
                chess_board_dict[next_move_notation] = chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - 2)]
                chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - 2)] = None
                is_valid_move = True

    display_chess_board()

if __name__ == "__main__":
    display_chess_board()
    white_to_move()