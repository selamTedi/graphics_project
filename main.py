import pygame
from maze import Maze

# SETTINGS 
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 15, 15
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator & Solver (DFS Stack)")
clock = pygame.time.Clock()

maze = Maze(ROWS, COLS, CELL_SIZE)

running = True
generating = True
solving = False

while running:
    clock.tick(60)

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GENERATION 
    if generating:
        generating = not maze.generate_step()

    # START SOLVER
    elif not solving and maze.generated:
        maze.prepare_solver()
        solving = True

    # SOLVING 
    else:
        maze.solve_step()

    maze.draw(screen)
    pygame.display.flip()

pygame.quit()