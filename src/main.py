from piece import *

cpg_data = chess_piece_general_data_dict # name shortcuts
cps_data = chess_piece_specific_data_dict 
chess_board_dict = {
    "a8": [cps_data["br1"]["name"], "br1"], "b8": [cps_data["bn1"]["name"], "bn1"], "c8": [cps_data["bb1"]["name"], "bb1"], "d8": [cps_data["bq"]["name"], "bq"], "e8": [cps_data["bk"]["name"], "bk"], "f8": [cps_data["bb2"]["name"], "bb2"], "g8": [cps_data["bn2"]["name"], "bn2"], "h8": [cps_data["br2"]["name"], "br2"], 
    "a7": [cps_data["bp1"]["name"], "bp1"], "b7": [cps_data["bp2"]["name"], "bp2"], "c7": [cps_data["bp3"]["name"], "bp3"], "d7": [cps_data["bp4"]["name"], "bp4"], "e7": [cps_data["bp5"]["name"], "bp5"], "f7": [cps_data["bp6"]["name"], "bp6"], "g7": [cps_data["bp7"]["name"], "bp7"], "h7": [cps_data["bp8"]["name"], "bp8"], 
    "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None, 
    "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None, 
    "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None, 
    "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None, 
    "a2": [cps_data["wp1"]["name"], "wp1"], "b2": [cps_data["wp2"]["name"], "wp2"], "c2": [cps_data["wp3"]["name"], "wp3"], "d2": [cps_data["wp4"]["name"], "wp4"], "e2": [cps_data["wp5"]["name"], "wp5"], "f2": [cps_data["wp6"]["name"], "wp6"], "g2": [cps_data["wp7"]["name"], "wp7"], "h2": [cps_data["wp8"]["name"], "wp8"], 
    "a1": [cps_data["wr1"]["name"], "wp1"], "b1": [cps_data["wn1"]["name"], "wn1"], "c1": [cps_data["wb1"]["name"], "wb1"], "d1": [cps_data["wq"]["name"], "wq"], "e1": [cps_data["wk"]["name"], "wk"], "f1": [cps_data["wb2"]["name"], "wb2"], "g1": [cps_data["wn2"]["name"], "wn2"], "h1": [cps_data["wr2"]["name"], "wr2"],
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
                chess_row += f" {cpg_data[chess_board_dict[letter + str(number)][0]]["unicode"]}  |"
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

    display_chess_board()
    black_to_move()

def black_to_move() -> None:
    display_chess_board()
    white_to_move()

if __name__ == "__main__":
    display_chess_board()
    white_to_move()