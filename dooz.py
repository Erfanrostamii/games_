import pygame
from pygame.locals import *

pygame.init()
window_size = (300, 300)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('DOOZ')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0 , 0)
GREEN = (0, 255, 0)
player, computer = "X", "O"
global current_player, board
current_player = player
board =  [" " for _ in range(9)]

def draw_board():
    window.fill(WHITE)
    font = pygame.font.Font(None, 40)
    pygame.draw.line(window, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(window, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(window, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(window, BLACK, (0, 200), (300, 200), 3)

    for i in range(9):
        x = (i % 3) * 100 + 50
        y = (i // 3) * 100 + 50
        if board[i] == "X":
            text = font.render("X", True, RED)
            window.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
        elif board[i] == "O":
            text = font.render("O", True, BLUE)
            window.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
    pygame.display.flip()
        
def check_click(position):
    global current_player
    x, y = position
    row = y // 100
    col = x // 100
    cell = row * 3 + col
    if board[cell] not in ["X", "O"]:
        board[cell] = current_player
        if current_player == player:
            current_player = computer
        else:
            current_player = player

def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [0,2,6,8]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 4 in possible_moves:
        move = 4
        return move

    edges_open = []
    for i in possible_moves:
        if i in [1,3,5,7]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)
    return move

def is_winner(bo, le):
    win_conditions = [(6, 7, 8), (3, 4, 5), (0, 1, 2), (6, 3, 0), 
                    (7, 4, 1), (8, 5, 2), (6, 4, 2), (8, 4, 0)]
    return any(bo[a] == le and bo[b] == le and bo[c] == le for a, b, c in win_conditions)

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def check_draw():
    if " " not in board and not is_winner(board, 'X') and not is_winner(board, 'O'):
        font = pygame.font.Font(None, 40)
        text = font.render("DRAW!", True, WHITE ,BLACK)
        window.blit(text, (150 - text.get_width() // 2, 150 - text.get_height() // 2))
        pygame.display.flip()
            
        pygame.time.wait(3000)
        reset_game()
            
def check_winner():
    winner = None
    if is_winner(board, 'X'):
        winner = 'player'
    elif is_winner(board, 'O'):
        winner = 'computer'

    if winner:
        font = pygame.font.Font(None, 40)
        color = GREEN if winner == 'player' else RED
        text = font.render(f"{winner.upper()} WINS!", True, color, BLACK)
        window.blit(text, (150 - text.get_width() // 2, 150 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        reset_game()
            

def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]    
    current_player = player
    draw_board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and current_player == player:
            check_click(pygame.mouse.get_pos())
            check_winner()
            check_draw() 
    if current_player == computer:
        move = computer_move()
        if move != 0:
            board[move] = 'O'
            check_winner()
        current_player = player
    draw_board()
    pygame.time.wait(100) 
pygame.quit()