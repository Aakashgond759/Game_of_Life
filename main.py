import pygame, sys
from simulation import Simulation
#from grid import Grid
#print("success")

pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750
CELL_SIZE = 6           # 25
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#simulation.grid.cells[4][0] = 1
#print(simulation.count_live_neighbours(simulation.grid, 5, 29))

#grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
#grid.cells[0][0] = 1

#Simulation Loop

while True:
    
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] //CELL_SIZE
            column = pos[0] //CELL_SIZE
            simulation.toggle_cell(row, column)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
                pygame.display.set_caption("Game of Life is running")
            elif event.key == pygame.K_SPACE:
                simulation.stop()
                pygame.display.set_caption("Game of Life is stopped")
            elif event.key == pygame.K_f:
                FPS +=2
            elif event.key == pygame.K_s:
                if FPS>5 : FPS -=2 
            elif event.key == pygame.K_r:
                simulation.create_random_state()
            elif event.key == pygame.K_c:
                simulation.clear()

    # 2. update state
    simulation.update()


    # 3. Drawing
    window.fill(GREY)
    simulation.draw(window)
    #grid.draw(window)

    pygame.display.update()
    clock.tick(FPS)
