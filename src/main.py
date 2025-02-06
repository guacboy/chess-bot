from chess_piece import chess_piece_specific_data_dict, chess_piece_general_data_dict

cpsdd = chess_piece_specific_data_dict # name shortcut
chess_board_dict = {
    "a8": cpsdd["br1"]["name"], "b8": cpsdd["bn1"]["name"], "c8": cpsdd["bb1"]["name"], "d8": cpsdd["bq"]["name"], "e8": cpsdd["bk"]["name"], "f8": cpsdd["bb2"]["name"], "g8": cpsdd["bn2"]["name"], "h8": cpsdd["br2"]["name"], 
    "a7": cpsdd["bp1"]["name"], "b7": cpsdd["bp2"]["name"], "c7": cpsdd["bp3"]["name"], "d7": cpsdd["bp4"]["name"], "e7": cpsdd["bp5"]["name"], "f7": cpsdd["bp6"]["name"], "g7": cpsdd["bp7"]["name"], "h7": cpsdd["bp8"]["name"], 
    "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None, 
    "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None, 
    "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None, 
    "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None, 
    "a2": cpsdd["wp1"]["name"], "b2": cpsdd["wp2"]["name"], "c2": cpsdd["wp3"]["name"], "d2": cpsdd["wp4"]["name"], "e2": cpsdd["wp5"]["name"], "f2": cpsdd["wp6"]["name"], "g2": cpsdd["wp7"]["name"], "h2": cpsdd["wp8"]["name"], 
    "a1": cpsdd["wr1"]["name"], "b1": cpsdd["wn1"]["name"], "c1": cpsdd["wb1"]["name"], "d1": cpsdd["wq"]["name"], "e1": cpsdd["wk"]["name"], "f1": cpsdd["wb2"]["name"], "g1": cpsdd["wn2"]["name"], "h1": cpsdd["wr2"]["name"],
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
                chess_row += f" {chess_piece_general_data_dict[chess_board_dict[letter + str(number)]]["unicode"]}  |"
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
        
        next_move_full_notation = next_move[-2:]
        next_move_letter_notation = next_move[-2]
        next_move_number_notation = next_move[-1]
        
        # if moving a pawn
        if next_move[0] not in piece_notation:
            if chess_board_dict[next_move_full_notation] is None:
                
                # moves the pawn up from inital placement
                chess_board_dict[next_move_full_notation] = chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - 2)]
                chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - 2)] = None
                is_valid_move = True

    display_chess_board()

if __name__ == "__main__":
    display_chess_board()
    white_to_move()