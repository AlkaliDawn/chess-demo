import pygame


def gridrender(current_disp, linearray_x, linearray_y):
    # Declare Variables
    width: int = pygame.Surface.get_width(current_disp)
    height: int = pygame.Surface.get_height(current_disp)

    # Render
    gridsize = 8
    for i in range(gridsize):
        pygame.draw.line(current_disp, (30, 32, 79), (linearray_x[i], 0), (linearray_x[i], height))  # Vertical Draw
        pygame.draw.line(current_disp, (30, 32, 79), (0, linearray_y[i]), (width, linearray_y[i]))  # Horizontal Draw


def line_array_gen(current_disp):
    # Declare Variables
    width: int = pygame.Surface.get_width(current_disp)
    height: int = pygame.Surface.get_height(current_disp)

    # Create Lists
    linearray_x = []
    linearray_y = []

    # Calculate x & y values, append to lists
    gridsize = 8
    for i in range(gridsize):
        linearray_x.append(width - i * (width / gridsize))
        linearray_y.append(height - i * (height / gridsize))

    # return arrays
    return (current_disp, linearray_x, linearray_y)


class ChessPiece:
    pos_x = 1
    pos_y = 1
    piece_type = 0
    alive = True

    def __init__(self, piece_type, current_disp):
        current_disp.blit()
