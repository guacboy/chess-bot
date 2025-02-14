from piece import *

cpg_data = chess_piece_general_data_dict # name shortcuts
cps_data = chess_piece_specific_data_dict 
chess_board_dict = {
    "a8": "br1", "b8": "bn1", "c8": "bb1", "d8": "bq", "e8": "bk", "f8": "bb2", "g8": "bn2", "h8": "br2", 
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8", 
    "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None, 
    "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None, 
    "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None, 
    "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None, 
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8", 
    "a1": "wp1", "b1": "wn1", "c1": "wb1", "d1": "wq", "e1": "wk", "f1": "wb2", "g1": "wn2", "h1": "wr2",
}
#TODO: you only need the piece ID

def display_chess_board() -> None:
    # prints the chess board with current pieces
    chess_row = ""
    print("  +----+----+----+----+----+----+----+----+")
    for number in range(8, 0, -1): # move number notation
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h"]: # move letter notation
            current_space = chess_board_dict[letter + str(number)]
            # if the current space is empty
            if current_space is None:
                # adds an empty space
                chess_row += "    |"
            # if the current space has a piece
            else:
                # adds the piece to the board
                chess_row += f" {cpg_data[cps_data[current_space]["name"]]["unicode"]}  |"
        print(f"{number} |{chess_row}")
        print("  +----+----+----+----+----+----+----+----+")
        chess_row = ""
    print("    a    b    c    d    e    f    g    h") # board letter notation

def white_to_move() -> None:
    piece_notation = ["K", "Q", "R", "B", "N"]
    is_valid_move = False
    while is_valid_move is False:
        next_move = input("YOUR TURN: ")
        
        # if the "next move" is empty
        if chess_board_dict[next_move] is None:
            # if moving a pawn
            if next_move[0] not in piece_notation:
                is_valid_move = pawn(chess_board_dict, next_move)
        else:
            invalid_move("Space occupied.")

    display_chess_board()
    black_to_move()

def black_to_move() -> None:
    # display_chess_board()
    white_to_move()

if __name__ == "__main__":
    display_chess_board()
    white_to_move()