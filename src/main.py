import pygame as pg

pg.init()

screen = pg.display.set_mode((920, 720))
clock = pg.time.Clock()

def app() -> None:
    """
    Pygame configurations.
    """
    
    is_running = True
    
    # list of objects
    objects = []
    
    pawn = pg.image.load("../src/assets/w_pawn.png")
    pawn = pg.transform.scale(pawn, (100, 100))
    pawn_collision = pawn.get_rect(center=(100, 100))
    objects.append([pawn, pawn_collision])
    bishop = pg.image.load("../src/assets/w_bishop.png")
    bishop = pg.transform.scale(bishop, (100, 100))
    bishop_collision = bishop.get_rect(center=(200, 100))
    objects.append([bishop, bishop_collision])

    is_moving = False
    
    while is_running:
        screen.fill("black") # color BG
        
        # loads the chess board
        load_board()
        
        # loads objects onto screen /
        # updates object's position
        for object in objects: 
            screen.blit(object[0], object[1])
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
            
            # if left-mouse button down
            if (event.type == pg.MOUSEBUTTONDOWN
                and event.button == 1):
                for object in objects:
                    # if cursor is inside an object
                    if object[1].collidepoint(event.pos):
                        object_collision = object[1]
                        # initialize object to be moved
                        is_moving = True
            # if left-mouse button is down
            # and mouse is moving
            elif (event.type == pg.MOUSEMOTION
                and is_moving):
                # moves object
                object_collision.move_ip(event.rel)
            # if left-mouse button is up
            elif (event.type == pg.MOUSEBUTTONUP
                and event.button == 1):
                is_moving = False
        
        pg.display.flip() # displays screen
        clock.tick(60)  # limits FPS to 60

    pg.quit()

def load_board() -> None:
    """
    Loads the chess board.
    """
    
    BOARD_COLOR_1 = "#769656"
    BOARD_COLOR_2 = "#EEEED2"
    board_color = BOARD_COLOR_1

    SQUARE_SIZE = 75
    square_x = SQUARE_INITIAL_X = 100 # initial board position
    
    # iterates through the # of columns
    for column in range(1, 9):
        # sets y position
        square_y = column * SQUARE_SIZE
        
        # alternates between the two colors
        # to make the checker theme
        if board_color == BOARD_COLOR_1:
            board_color = BOARD_COLOR_2
        elif board_color == BOARD_COLOR_2:
            board_color = BOARD_COLOR_1
        
        # iterates through the # of rows
        for row in range(1, 9):
            # set x position
            square_x = SQUARE_INITIAL_X + (row * SQUARE_SIZE)
            
            # alternates between the two colors
            # to make the checker theme
            if board_color == BOARD_COLOR_1:
                board_color = BOARD_COLOR_2
            elif board_color == BOARD_COLOR_2:
                board_color = BOARD_COLOR_1
                
            # initializes the rectangle
            square = pg.Rect(square_x, square_y, SQUARE_SIZE, SQUARE_SIZE)
            pg.draw.rect(screen, board_color, square)
        # resets x position
        square_x = SQUARE_INITIAL_X

if __name__ == "__main__":
    
    app()