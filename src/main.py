import pygame as pg

pg.init()

screen = pg.display.set_mode((920, 720))
clock = pg.time.Clock()

def app() -> None:
    """
    Pygame configurations.
    """
    
    is_running = True
    
    # list of notations
    notations = load_board() # loads the chess board
    # list of objects
    objects = load_objects(notations) # loads the pieces

    is_moving = False
    
    while is_running:
        screen.fill("black") # color BG
        
        load_board() # loads the chess board
        
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

def load_objects(notations: list) -> list:
    """
    Loads the chess pieces.
    """
    
    b_rook1, b_rook1_collision = "b_rook", None
    b_knight1, b_knight1_collision = "b_knight", None
    b_bishop1, b_bishop1_collision = "b_bishop", None
    b_queen1, b_queen1_collision = "b_queen", None
    b_king1, b_king1_collision = "b_king", None
    b_bishop2, b_bishop2_collision = "b_bishop", None
    b_knight2, b_knight2_collision = "b_knight", None
    b_rook2, b_rook2_collision = "b_rook", None
    b_pawn1, b_pawn1_collision = "b_pawn", None
    b_pawn2, b_pawn2_collision = "b_pawn", None
    b_pawn3, b_pawn3_collision = "b_pawn", None
    b_pawn4, b_pawn4_collision = "b_pawn", None
    b_pawn5, b_pawn5_collision = "b_pawn", None
    b_pawn6, b_pawn6_collision = "b_pawn", None
    b_pawn7, b_pawn7_collision = "b_pawn", None
    b_pawn8, b_pawn8_collision = "b_pawn", None
    
    w_pawn1, w_pawn1_collision = "w_pawn", None
    w_pawn2, w_pawn2_collision = "w_pawn", None
    w_pawn3, w_pawn3_collision = "w_pawn", None
    w_pawn4, w_pawn4_collision = "w_pawn", None
    w_pawn5, w_pawn5_collision = "w_pawn", None
    w_pawn6, w_pawn6_collision = "w_pawn", None
    w_pawn7, w_pawn7_collision = "w_pawn", None
    w_pawn8, w_pawn8_collision = "w_pawn", None
    w_rook1, w_rook1_collision = "w_rook", None
    w_knight1, w_knight1_collision = "w_knight", None
    w_bishop1, w_bishop1_collision = "w_bishop", None
    w_queen1, w_queen1_collision = "w_queen", None
    w_king1, w_king1_collision = "w_king", None
    w_bishop2, w_bishop2_collision = "w_bishop", None
    w_knight2, w_knight2_collision = "w_knight", None
    w_rook2, w_rook2_collision = "w_rook", None
    
    objects = [
        [b_rook1, b_rook1_collision],
        [b_knight1, b_knight1_collision],
        [b_bishop1, b_bishop1_collision],
        [b_queen1, b_queen1_collision],
        [b_king1, b_king1_collision],
        [b_bishop2, b_bishop2_collision],
        [b_knight2, b_knight2_collision],
        [b_rook2, b_rook2_collision],
        [b_pawn1, b_pawn1_collision],
        [b_pawn2, b_pawn2_collision],
        [b_pawn3, b_pawn3_collision],
        [b_pawn4, b_pawn4_collision],
        [b_pawn5, b_pawn5_collision],
        [b_pawn6, b_pawn6_collision],
        [b_pawn7, b_pawn7_collision],
        [b_pawn8, b_pawn8_collision],
        
        [w_pawn1, w_pawn1_collision],
        [w_pawn2, w_pawn2_collision],
        [w_pawn3, w_pawn3_collision],
        [w_pawn4, w_pawn4_collision],
        [w_pawn5, w_pawn5_collision],
        [w_pawn6, w_pawn6_collision],
        [w_pawn7, w_pawn7_collision],
        [w_pawn8, w_pawn8_collision],
        [w_rook1, w_rook1_collision],
        [w_knight1, w_knight1_collision],
        [w_bishop1, w_bishop1_collision],
        [w_queen1, w_queen1_collision],
        [w_king1, w_king1_collision],
        [w_bishop2, w_bishop2_collision],
        [w_knight2, w_knight2_collision],
        [w_rook2, w_rook2_collision],
    ]
    
    starting_notations = notations[0:16] + notations[-16:]
    # TODO: place objects into starting positions
    
    for object in objects:
        # loads the image      
        object[0] = pg.image.load(f"../src/assets/{object[0]}.png")
        # rescales the image
        object[0] = pg.transform.scale(object[0], (75, 75))  
        # initializes the image 
        object[1] = object[0].get_rect(center=(100, 100))
    
    return objects

def load_board() -> list:
    """
    Loads the chess board.
    """
    
    a8 = None
    b8 = None
    c8 = None
    d8 = None
    e8 = None
    f8 = None
    g8 = None
    h8 = None
    a7 = None
    b7 = None
    c7 = None
    d7 = None
    e7 = None
    f7 = None
    g7 = None
    h7 = None
    a6 = None
    b6 = None
    c6 = None
    d6 = None
    e6 = None
    f6 = None
    g6 = None
    h6 = None
    a5 = None
    b5 = None
    c5 = None
    d5 = None
    e5 = None
    f5 = None
    g5 = None
    h5 = None
    a4 = None
    b4 = None
    c4 = None
    d4 = None
    e4 = None
    f4 = None
    g4 = None
    h4 = None
    a3 = None
    b3 = None
    c3 = None
    d3 = None
    e3 = None
    f3 = None
    g3 = None
    h3 = None
    a2 = None
    b2 = None
    c2 = None
    d2 = None
    e2 = None
    f2 = None
    g2 = None
    h2 = None
    a1 = None
    b1 = None
    c1 = None
    d1 = None
    e1 = None
    f1 = None
    g1 = None
    h1 = None
    
    notations = [
        a8,
        b8,
        c8,
        d8,
        e8,
        f8,
        g8,
        h8,
        a7,
        b7,
        c7,
        d7,
        e7,
        f7,
        g7,
        h7,
        a6,
        b6,
        c6,
        d6,
        e6,
        f6,
        g6,
        h6,
        a5,
        b5,
        c5,
        d5,
        e5,
        f5,
        g5,
        h5,
        a4,
        b4,
        c4,
        d4,
        e4,
        f4,
        g4,
        h4,
        a3,
        b3,
        c3,
        d3,
        e3,
        f3,
        g3,
        h3,
        a2,
        b2,
        c2,
        d2,
        e2,
        f2,
        g2,
        h2,
        a1,
        b1,
        c1,
        d1,
        e1,
        f1,
        g1,
        h1,
    ]
    
    BOARD_COLOR_1 = "#769656"
    BOARD_COLOR_2 = "#EEEED2"
    board_color = BOARD_COLOR_1

    SQUARE_SIZE = 75
    SQUARE_INITIAL_Y = -15 # initial board y position
    SQUARE_INITIAL_X = 100 # initial board x position
    notation_idx = 0
    
    # iterates through the # of columns
    for column in range(1, 9):
        # sets y position
        square_y = SQUARE_INITIAL_Y + (column * SQUARE_SIZE)
        
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
            notations[notation_idx] = (square.x, square.y) # notation coordinates
            pg.draw.rect(screen, board_color, square)
            
            # iterates to the next notation
            notation_idx += 1
            
        # resets x position
        square_x = SQUARE_INITIAL_X
    
    return notations

if __name__ == "__main__":
    app()