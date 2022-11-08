import pygame

# Declare Variables

width: int = pygame.Surface.get_width(DISPLAY)
height: int = pygame.Surface.get_height(DISPLAY)

gridsize = 8

line_array_x = []
line_array_y = []


def grid_line_render(current_disp):


    # Access Global Variables
    global line_array_x
    global line_array_y

    # Calculate x & y values, append to lists
    line_array_x, line_array_y = [], []
    for i in range(gridsize):
        line_array_x.append(width - i * (width / gridsize))
        line_array_y.append(height - i * (height / gridsize))

    print(pygame.mouse.get_pos())
    print(
        "X array: " + str(line_array_x[0]) + " " + str(line_array_x[7]) + "  Y array: " + str(line_array_y[0]) + " " + str(
            line_array_y[7]) + "\n")

    # Render
    for i in range(gridsize):
        pygame.draw.line(current_disp, (30, 32, 79), (line_array_x[i], 0), (line_array_x[i], height))  # Vertical Draw
        pygame.draw.line(current_disp, (30, 32, 79), (0, line_array_y[i]), (width, line_array_y[i]))  # Horizontal Draw


class ChessPiece:
    pos_x = 1
    pos_y = 1
    alive = True


def checker_render:


def import_img():
    PAWN_BLACK = pygame.image.load("P_B.png")
    PAWN_WHITE = pygame.image.load("P_W.png")
    ROOK_BLACK = pygame.image.load("R_B.png")
    ROOK_WHITE = pygame.image.load("R_W.png")
    BISHOP_BLACK = pygame.image.load("B_B.png")
    BISHOP_WHITE = pygame.image.load("B_W.png")
    KNIGHT_BLACK = pygame.image.load("N_B.png")
    KNIGHT_WHITE = pygame.image.load("N_W.png")
    KING_BLACK = pygame.image.load("K_B.png")
    KING_WHITE = pygame.image.load("K_W.png")
    QUEEN_BLACK = pygame.image.load("Q_B.png")
    QUEEN_WHITE = pygame.image.load("Q_W.png")


if __name__ == '__main__':
    pygame.init()  # init pygame modules

    import_img()  # import chess piece icons

    SEPIA = (128, 97, 60)
    DARK_SEPIA = (28, 19, 9)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    DISPLAY = pygame.display.set_mode((640, 480), pygame.RESIZABLE)  # initialize display

    pygame.display.set_caption("Chess in Pygame")  # change name of window

    run = True

    while run:  # START OF MAIN LOOP

        pygame.event.pump()  # OS Connection

        for event in pygame.event.get():  # Quit Case
            if event.type == pygame.QUIT:
                run = False

        DISPLAY.fill(BLACK)



        grid_line_render(DISPLAY)  # Render and compute grid lines

        pygame.display.update()
