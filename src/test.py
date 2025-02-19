from main import *
from piece import *

def run_all_test() -> None:
    test_list = [
        test_pawn()
    ]
    
    # iterates through the list of test results
    for idx, result_list in enumerate(test_list):
        test_passed_count = 0
        # iterates through the inner list of test results
        # to determine if the overall test has passed
        for result in result_list:
            # if individual test has passed, increment count
            if result.endswith("PASSED"):
                test_passed_count += 1
            # if individual test has failed, break loop
            else:
                test_list[idx] = result
                break
            
        # if all individual tests have passed,
        # then the overall test has passed
        if test_passed_count == len(result_list):
            test_list[idx] = "TEST PASSED"
        # if at least one individual test failed,
        # then break loop
        else:
            break
    
    # prints out the OVERALL test results
    for result in test_list:
        print(f"--{result}--")
        # display one error at a time
        if result.endswith("FAILED"):
            break

def test_pawn() -> list:
    # tests if pawn can move two spaces, then one space forward
    def can_pawn_move() -> str:
        create_chess_board()
        
        for notation in ["a4", "a5"]:
            white_to_move(True, notation)
            
        if chess_board_dict.get("a5") == "wp1":
            return "TEST PASSED"
        else:
            # pawn did not move properly
            return "can_pawn_move() FAILED"
        
    # tests if pawn can capture right, then left
    def can_pawn_capture() -> str:
        create_chess_board([["a6", "wp1"]])
                
        for notation in ["axb7", "bxa8"]:
            white_to_move(True, notation)
            
        if chess_board_dict.get("a8") == "wp1":
            return "TEST PASSED"
        else:
            # pawn did not capture properly
            return "can_pawn_move() FAILED"
        
    #TODO: can a pawn enpassent
    
    return can_pawn_move(), can_pawn_capture()

if __name__ == "__main__":
    run_all_test()