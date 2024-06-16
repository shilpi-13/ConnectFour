import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
ROWS = 6
COLS = 7
TILESIZE = 100  # Size of each square tile
WIDTH = COLS * TILESIZE
HEIGHT = (ROWS + 1) * TILESIZE  # Extra row for dropping pieces
RADIUS = TILESIZE // 2 - 5
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
SQUARESIZE = TILESIZE

# Initialize the game board (6x7 grid)
board = np.zeros((ROWS, COLS))

# Pygame screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four Game")

# Function to draw the board
def draw_board(board):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c * TILESIZE, r * TILESIZE + TILESIZE, TILESIZE, TILESIZE))
            pygame.draw.circle(screen, BLACK, (c * TILESIZE + TILESIZE // 2, r * TILESIZE + TILESIZE + TILESIZE // 2), RADIUS)

    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * TILESIZE + TILESIZE // 2, HEIGHT - r * TILESIZE - TILESIZE // 2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * TILESIZE + TILESIZE // 2, HEIGHT - r * TILESIZE - TILESIZE // 2), RADIUS)
    pygame.display.update()

# Function to drop a piece into the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check if the column is valid for placing a piece
def is_valid_location(board, col):
    return board[ROWS-1][col] == 0

# Function to get the next available row for a piece in a column
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

# Function to check for a win condition
def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

# Main game loop
def main():
    turn = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Player 1's turn
                if turn % 2 == 0:
                    mouseX = event.pos[0]
                    col = mouseX // TILESIZE

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            print("Player 1 wins!!")
                            pygame.quit()
                            sys.exit()

                # Player 2's turn
                else:
                    mouseX = event.pos[0]
                    col = mouseX // TILESIZE

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            print("Player 2 wins!!")
                            pygame.quit()
                            sys.exit()

                turn += 1
                print(board)
                draw_board(board)

if __name__ == "__main__":
    main()
