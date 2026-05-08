import pygame
import random

class Maze:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        #  WALLS 
        self.northWall = [[1 for _ in range(cols)] for _ in range(rows)]
        self.eastWall = [[1 for _ in range(cols)] for _ in range(rows)]

        # GENERATION 
        self.visited_gen = [[False for _ in range(cols)] for _ in range(rows)]
        self.gen_stack = []

        # START (left edge)
        self.start = (random.randint(0, rows - 1), 0)
        self.gen_stack.append(self.start)
        self.visited_gen[self.start[0]][self.start[1]] = True

        # END (right edge)
        self.end = (random.randint(0, rows - 1), cols - 1)

        # OPENINGS (important for correctness)
        self.eastWall[self.end[0]][self.end[1]] = 0
        self.eastWall[self.start[0]][self.start[1]] = 0

        self.generated = False

        # SOLVER
        self.visited_sol = [[False for _ in range(cols)] for _ in range(rows)]
        self.sol_stack = []
        self.dead = [[False for _ in range(cols)] for _ in range(rows)]

    
    # REMOVE WALL
    
    def remove_wall(self, r1, c1, r2, c2):
        if r1 == r2:
            if c1 < c2:
                self.eastWall[r1][c1] = 0
            else:
                self.eastWall[r2][c2] = 0
        else:
            if r1 < r2:
                self.northWall[r2][c2] = 0
            else:
                self.northWall[r1][c1] = 0

    
    # GENERATION (DFS STACK + BONUS CYCLES)
    
    def generate_step(self):
        if not self.gen_stack:
            self.generated = True
            return True

        r, c = self.gen_stack[-1]

        neighbors = []

        if r > 0 and not self.visited_gen[r - 1][c]:
            neighbors.append((r - 1, c))
        if r < self.rows - 1 and not self.visited_gen[r + 1][c]:
            neighbors.append((r + 1, c))
        if c > 0 and not self.visited_gen[r][c - 1]:
            neighbors.append((r, c - 1))
        if c < self.cols - 1 and not self.visited_gen[r][c + 1]:
            neighbors.append((r, c + 1))

        if neighbors:
            nr, nc = random.choice(neighbors)

            self.remove_wall(r, c, nr, nc)
            self.visited_gen[nr][nc] = True
            self.gen_stack.append((nr, nc))

            # BONUS: 1/20 cycle creation 
            if random.randint(1, 20) == 1:
                all_neighbors = []

                if r > 0:
                    all_neighbors.append((r - 1, c))
                if r < self.rows - 1:
                    all_neighbors.append((r + 1, c))
                if c > 0:
                    all_neighbors.append((r, c - 1))
                if c < self.cols - 1:
                    all_neighbors.append((r, c + 1))

                nr2, nc2 = random.choice(all_neighbors)
                self.remove_wall(r, c, nr2, nc2)

        else:
            self.gen_stack.pop()

        return False

    
    # SOLVER SETUP
    
    def prepare_solver(self):
        self.sol_stack = [self.start]
        self.visited_sol[self.start[0]][self.start[1]] = True

    
    # SOLVER (DFS BACKTRACK + RANDOM MOVES)
    
    def solve_step(self):
        if not self.sol_stack:
            return

        r, c = self.sol_stack[-1]

        if (r, c) == self.end:
            return

        moves = []

        if c < self.cols - 1 and self.eastWall[r][c] == 0:
            moves.append((r, c + 1))
        if r < self.rows - 1 and self.northWall[r + 1][c] == 0:
            moves.append((r + 1, c))
        if c > 0 and self.eastWall[r][c - 1] == 0:
            moves.append((r, c - 1))
        if r > 0 and self.northWall[r][c] == 0:
            moves.append((r - 1, c))

        random.shuffle(moves)

        moved = False

        for nr, nc in moves:
            if not self.visited_sol[nr][nc]:
                self.sol_stack.append((nr, nc))
                self.visited_sol[nr][nc] = True
                moved = True
                break

        if not moved:
            r2, c2 = self.sol_stack.pop()
            self.dead[r2][c2] = True

    
    # DRAW
    
    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                x = c * self.cell_size
                y = r * self.cell_size

                # DEAD END (BLUE)
                if self.dead[r][c]:
                    pygame.draw.rect(screen, (0, 0, 255),
                                     (x, y, self.cell_size, self.cell_size))

                # GENERATOR (GREEN)
                if self.gen_stack and (r, c) == self.gen_stack[-1] and not self.generated:
                    pygame.draw.circle(screen, (0, 255, 0),
                                       (x + self.cell_size // 2,
                                        y + self.cell_size // 2),
                                       self.cell_size // 4)

                # SOLVER (RED)
                if self.sol_stack and (r, c) == self.sol_stack[-1] and self.generated:
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (x + self.cell_size // 2,
                                        y + self.cell_size // 2),
                                       self.cell_size // 4)

                # WALLS
                if self.northWall[r][c]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (x, y),
                                     (x + self.cell_size, y), 2)

                if self.eastWall[r][c]:
                    pygame.draw.line(screen, (0, 0, 0),
                                     (x + self.cell_size, y),
                                     (x + self.cell_size, y + self.cell_size), 2)

        # BORDER
        pygame.draw.rect(screen, (0, 0, 0),
                         (0, 0,
                          self.cols * self.cell_size,
                          self.rows * self.cell_size), 2)

        # START (GREEN BLOCK)
        sx, sy = self.start[1]*self.cell_size, self.start[0]*self.cell_size
        ex, ey = self.end[1]*self.cell_size, self.end[0]*self.cell_size

        pygame.draw.rect(screen, (0, 200, 0), (sx, sy, self.cell_size, self.cell_size))
        pygame.draw.rect(screen, (200, 0, 0), (ex, ey, self.cell_size, self.cell_size))