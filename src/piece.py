chess_piece_general_data_dict = {
    "black_king": {
        "unicode": "♚"},
    "black_queen": {
        "unicode": "♛"},
    "black_rook": {
        "unicode": "♜"},
    "black_bishop": {
        "unicode": "♝"},
    "black_knight": {
        "unicode": "♞"},
    "black_pawn": {
        "unicode": "♟"},
    
    "white_king": {
        "unicode": "♔"},
    "white_queen": {
        "unicode": "♕"},
    "white_rook": {
        "unicode": "♖"},
    "white_bishop": {
        "unicode": "♗"},
    "white_knight": {
        "unicode": "♘"},
    "white_pawn": {
        "unicode": "♙"},
}

chess_piece_specific_data_dict = {
    "br1": {
        "name": "black_rook",
    },
    "bn1": {
        "name": "black_knight",
    },
    "bb1": {
        "name": "black_bishop",
    },
    "bq": {
        "name": "black_queen",
    },
    "bk": {
        "name": "black_king",
    },
    "bb2": {
        "name": "black_bishop",
    },
    "bn2": {
        "name": "black_knight",
    },
    "br2": {
        "name": "black_rook",
    },
    "bp1": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    "bp2": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    "bp3": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    "bp4": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    "bp5": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    "bp6": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    "bp7": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    "bp8": {
        "name": "black_pawn",
        "can_move_two_spaces": True,
    },
    
    "wr1": {
        "name": "white_rook",
    },
    "wn1": {
        "name": "white_knight",
    },
    "wb1": {
        "name": "white_bishop",
    },
    "wq": {
        "name": "white_queen",
    },
    "wk": {
        "name": "white_king",
    },
    "wb2": {
        "name": "white_bishop",
    },
    "wn2": {
        "name": "white_knight",
    },
    "wr2": {
        "name": "white_rook",
    },
    "wp1": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
    "wp2": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
    "wp3": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
    "wp4": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
    "wp5": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
    "wp6": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
    "wp7": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
    "wp8": {
        "name": "white_pawn",
        "can_move_two_spaces": True,
    },
}

cpg_data = chess_piece_general_data_dict # name shortcuts
cps_data = chess_piece_specific_data_dict

def invalid_move(explanation: str="") -> bool:
    print("*INVALID MOVE*", explanation)
    return False 

def pawn(chess_board_dict: dict, next_move: str) -> bool:    
    is_pawn = False
    
    #TODO: refactor code to make it smaller; use get()
    # if attempting to capture a piece
    if len(next_move) == 4 and next_move[1] == "x":
        next_move_location_notation = next_move[-2:] # exmaple: e4
        next_move_piece_notation = next_move[0] # example: d
        next_move_letter_notation = next_move[2] # exmaple: e
        next_move_number_notation = next_move[3] # example: 4
        
        if next_move_piece_notation == next_move_letter_notation:
            return invalid_move("Pawn can not capture forward.")
        
        # locates pawn
        is_pawn = cps_data[chess_board_dict.get(next_move_piece_notation + str(int(next_move_number_notation) - 1))]["name"].endswith("pawn")

        
        if is_pawn:
            # captures piece
            chess_board_dict[next_move_location_notation] = chess_board_dict.get(next_move_piece_notation + str(int(next_move_number_notation) - 1))
            # updates previous space to empty
            chess_board_dict[next_move_piece_notation + str(int(next_move_number_notation) - 1)] = None
        else:
            return invalid_move("No pawn found.")
    else:
        
        next_move_letter_notation = next_move[0] # example: e
        next_move_number_notation = next_move[1] # example: 4
        
        # scans one and two spaces behind "next move" for a pawn
        for check_backwards in range(1, 3):
            try:
                # locates pawn
                is_pawn = cps_data[chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - check_backwards)]]["name"].endswith("pawn")
            # ignores NoneType
            except AttributeError:
                continue
            # ignores NoneType
            except TypeError:
                continue
            # ignores NoneType
            except KeyError:
                continue
            
            if is_pawn:                    
                can_move_two_spaces = cps_data[chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - check_backwards)]]["can_move_two_spaces"]
                
                # attempting to move a pawn two spaces if it has already moved from inital position
                if check_backwards == 2 and can_move_two_spaces is False:
                    return invalid_move("Pawn can not move two spaces.")
                
                # updates pawn eligbility to move two spaces after first move
                cps_data[chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - check_backwards)]]["can_move_two_spaces"] = False

                # pawn has been found, break loop
                go_back_from_next_move = check_backwards
                break
        
        try:
            # moves the pawn up
            # finds a pawn x spaces behind the "next move"
            chess_board_dict[next_move] = chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - go_back_from_next_move)]
            # updates previous space to empty
            chess_board_dict[next_move_letter_notation + str(int(next_move_number_notation) - go_back_from_next_move)] = None
        except UnboundLocalError:
            return invalid_move("No pawn found.")
    
    #TODO: pawn enpassent

    return True # valid move
