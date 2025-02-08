from chess_piece import chess_piece_specific_data_dict, chess_piece_general_data_dict

cps_data = chess_piece_specific_data_dict # name shortcuts
cpg_data = chess_piece_general_data_dict
chess_board_dict = {
    "a8": cps_data["br1"]["name"], "b8": cps_data["bn1"]["name"], "c8": cps_data["bb1"]["name"], "d8": cps_data["bq"]["name"], "e8": cps_data["bk"]["name"], "f8": cps_data["bb2"]["name"], "g8": cps_data["bn2"]["name"], "h8": cps_data["br2"]["name"], 
    "a7": cps_data["bp1"]["name"], "b7": cps_data["bp2"]["name"], "c7": cps_data["bp3"]["name"], "d7": cps_data["bp4"]["name"], "e7": cps_data["bp5"]["name"], "f7": cps_data["bp6"]["name"], "g7": cps_data["bp7"]["name"], "h7": cps_data["bp8"]["name"], 
    "a6": None, "b6": None, "c6": None, "d6": None, "e6": None, "f6": None, "g6": None, "h6": None, 
    "a5": None, "b5": None, "c5": None, "d5": None, "e5": None, "f5": None, "g5": None, "h5": None, 
    "a4": None, "b4": None, "c4": None, "d4": None, "e4": None, "f4": None, "g4": None, "h4": None, 
    "a3": None, "b3": None, "c3": None, "d3": None, "e3": None, "f3": None, "g3": None, "h3": None, 
    "a2": cps_data["wp1"]["name"], "b2": cps_data["wp2"]["name"], "c2": cps_data["wp3"]["name"], "d2": cps_data["wp4"]["name"], "e2": cps_data["wp5"]["name"], "f2": cps_data["wp6"]["name"], "g2": cps_data["wp7"]["name"], "h2": cps_data["wp8"]["name"], 
    "a1": cps_data["wr1"]["name"], "b1": cps_data["wn1"]["name"], "c1": cps_data["wb1"]["name"], "d1": cps_data["wq"]["name"], "e1": cps_data["wk"]["name"], "f1": cps_data["wb2"]["name"], "g1": cps_data["wn2"]["name"], "h1": cps_data["wr2"]["name"],
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
                chess_row += f" {cpg_data[chess_board_dict[letter + str(number)]]["unicode"]}  |"
        print(f"{number} |{chess_row}")
        print("  +----+----+----+----+----+----+----+----+")
        chess_row = ""
    print("    a    b    c    d    e    f    g    h") # board letter notation

def white_to_move() -> None:
    piece_notation = ["K", "Q", "R", "B", "N"]
    is_valid_move = False
    while is_valid_move is False:
        next_move = input("YOUR TURN: ")
        
        next_move_full_notation = next_move[-2:] # example: e4
        next_move_letter_notation = next_move[-2] # example: e
        next_move_number_notation = next_move[-1] # example: 4
        
        # if moving a pawn
        if next_move[0] not in piece_notation:
            # if the "next move" is empty
            if chess_board_dict[next_move_full_notation] is None:
                # scans one and two spaces behind "next move" for a pawn
                for look_for_pawn in range(1, 3):
                    try:
                        chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - look_for_pawn)].endswith("pawn")
                    # ignores NoneType
                    except AttributeError:
                        pass
                    # pawn has been found, break loop
                    else:
                        go_back_from_next_move = look_for_pawn
                        break
                
                # moves the pawn up
                # finds a pawn x spaces behind the "next move"
                chess_board_dict[next_move_full_notation] = chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - go_back_from_next_move)]
                # updates previous space to empty
                chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - go_back_from_next_move)] = None
                is_valid_move = True

    display_chess_board()
    # black_to_move()

def black_to_move() -> None:
    display_chess_board()
    white_to_move()

if __name__ == "__main__":
    display_chess_board()
    white_to_move()