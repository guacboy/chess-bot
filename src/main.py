import pygame

pygame.init()

screen = pygame.display.set_mode((720, 620))
clock = pygame.time.Clock()

def app() -> None:
    is_running = True
    
    # list of objects
    objects = []
    rectangle = pygame.Rect(100, 100, 100, 200)
    objects.append(rectangle)
    square = pygame.Rect(500, 100, 100, 100)
    objects.append(square)
    
    is_moving = False
    
    while is_running:
        screen.fill("black") # color BG
        
        # loads objects onto screen
        pygame.draw.rect(screen, (0, 0, 255), rectangle, 0)
        pygame.draw.rect(screen, (0, 255, 0), square, 0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            # if left-mouse button down
            if (event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1):
                # iterates through the list of objects
                for object in objects:
                    # if cursor is inside an object
                    if object.collidepoint(event.pos):
                        # initialize object to be moved
                        object_to_be_moved = object
                        is_moving = True
            # if left-mouse button is down
            # and mouse is moving
            elif (event.type == pygame.MOUSEMOTION
                and is_moving):
                # moves object
                object_to_be_moved.move_ip(event.rel)
            # if left-mouse button is up
            elif (event.type == pygame.MOUSEBUTTONUP
                and event.button == 1):
                is_moving = False

        if is_moving:
            # updates objects position
            pygame.draw.rect(screen, (0, 0, 255), object_to_be_moved, 0)
        
        pygame.display.flip() # displays screen
        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    app()