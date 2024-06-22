import tkinter as tk
import pygame
from pygame.locals import *
import random
import time     
import sys

def play_rock():
    pygame.init()
    width , height = 1080 , 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('سنگ کاغذ قیچی')

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont(None, 55)

    choices = ["rock", "paper", "scissors"]
    
    def get_computer_choice():
        return random.choice(choices)

    def get_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'Draw'
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            return 'You won!'
        else:
            return 'You lost!'

    def game_loop():
        user_choice = None
        game_over = False
        player_score = 0
        computer_score = 0


        while not game_over:
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        user_choice = "rock"
                    elif event.key == pygame.K_p:
                        user_choice = "paper"
                    elif event.key == pygame.K_s:
                        user_choice = "scissors"
                    elif event.key ==pygame.K_q:
                        pygame.quit()

            if user_choice:
                computer_choice = get_computer_choice()
                winner = get_winner(user_choice, computer_choice)
                user_choice_text = font.render(f'Your choice: {user_choice}', True, (250,200,0))
                computer_choice_text = font.render(f'computer choice: {computer_choice}', True, (0,200,250))
                if winner == 'You won!' :
                    player_score += 1
                    rang = (0,250,0)
                elif winner == 'You lost!' :
                    computer_score += 1
                    rang = (250,0,0)
                else:
                    rang = BLACK
                winner_text = font.render(winner, True, rang)
                Pscore_text = font.render(f"Player Score : {player_score}",True,(0,250,0))
                Cscore_text = font.render(f"Computer Score : {computer_score}",True,(250 , 0 , 0))

                chosse = font.render(f"press 'r' for rock , press 'p' for paper , press 's' for scissors", True,(250,0,250))
                khoroj = font.render('press \'q\' for Quit', True , (250,0,250))
                screen.blit(chosse, (10, 10))
                screen.blit(khoroj,(10,50))
                screen.blit(user_choice_text, (50, 150))
                screen.blit(computer_choice_text, (50, 250))
                screen.blit(winner_text, (50, 350))
                screen.blit(Pscore_text , (600 , 150))
                screen.blit(Cscore_text , (600 , 250))
                

                pygame.display.update()
                pygame.time.wait(2000)
                user_choice = None
    chosse1 = font.render(" press 'r' for rock ", True,WHITE)
    chosse2 = font.render(" press 'p' for paper ", True,WHITE)
    chosse3 = font.render(" press 's' for scissors", True,WHITE)
    screen.blit(chosse1,(100,120))
    screen.blit(chosse2,(100,220))
    screen.blit(chosse3,(100,320))
    pygame.display.update()
    game_loop()

def play_snake():

    pygame.init() 
    
    screen_width = 1000 
    screen_height = 600 
    screen = pygame.display.set_mode((screen_width, screen_height)) 
    pygame.display.set_caption("Snake Game") 
    
    white = (255, 255, 255) 
    yellow = (255, 255, 102) 
    black = (0, 0, 0) 
    red = (213, 50, 80) 
    green = (0, 255, 0) 
    blue = (50, 153, 213) 
    
    snake_block = 20 
    snake_speed = 12 

    clock = pygame.time.Clock() 
    
    def display_score(score): 
        font = pygame.font.SysFont(None, 30) 
        text = font.render("SCORE:" + str(score), True, white, black) 
        screen.blit(text, (5, 5)) 
    
    def draw_snake(snake_list): 
        for x, y in snake_list: 
            pygame.draw.rect(screen, red, [x, y, snake_block, snake_block]) 
    
    def message(msg, color): 
        font_style = pygame.font.SysFont(None, 50) 
        rendered_msg = font_style.render(msg, True, color) 
        screen.blit(rendered_msg, [screen_width / 8, screen_height / 3]) 
    
    game_over = False 
    game_close = False 

    snake_list = [] 
    length_of_snake = 1 
    snake_x = screen_width / 2 
    snake_y = screen_height / 2 
    snake_x_change = 0 
    snake_y_change = 0 

    food_x = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0 
    food_y = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0 

    while not game_over: 
        while game_close: 
            screen.fill(white) 
            message("You Lost! Press 'C' for Play Again or 'Q' for Quit ", red) 
            display_score(length_of_snake - 1) 
            pygame.display.update() 
    
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q: 
                        game_over = True 
                        game_close = False 
                    elif event.key == pygame.K_c: 
                        play_snake()
                    
                    

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_over = True 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    snake_x_change = -snake_block 
                    snake_y_change = 0 
                elif event.key == pygame.K_RIGHT: 
                    snake_x_change = snake_block 
                    snake_y_change = 0 
                elif event.key == pygame.K_UP: 
                    snake_y_change = -snake_block 
                    snake_x_change = 0 
                elif event.key == pygame.K_DOWN: 
                    snake_y_change = snake_block 
                    snake_x_change = 0 
                elif event.key == pygame.K_q:
                    game_over = True

        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0: 
            game_close = True 

        snake_x += snake_x_change 
        snake_y += snake_y_change 
        screen.fill(white) 
        pygame.draw.rect(screen, black, [food_x, food_y, snake_block, snake_block]) 
        snake_head = [snake_x, snake_y] 
        snake_list.append(snake_head) 

        if len(snake_list) > length_of_snake: 
            del snake_list[0] 

        for segment in snake_list[:-1]: 
            if segment == snake_head: 
                game_close = True 

        draw_snake(snake_list) 
        display_score(length_of_snake - 1) 

        pygame.display.update() 

        if snake_x == food_x and snake_y == food_y: 
            food_x = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0 
            food_y = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0 
            length_of_snake += 1 

        clock.tick(snake_speed) 

    pygame.quit() 


def play_doz():
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

def show_game_names():
    root = tk.Tk()
    root.title("انواع بازی")

    game_names = ["سنگ کاغذ قیچی", "مار", "دوز"]

    def close_window():
        root.destroy()

    frame = tk.Frame(root)
    frame.pack(pady=20)

    for i, name in enumerate(game_names):
        button = tk.Button(frame, text=name, command=lambda n=name: play_game(n), height=3, width=20, bg="yellow", font=("Arial", 14, "bold"))
        button.grid(row=i, column=0, pady=40)  

    close_button = tk.Button(root, text="بستن", command=close_window, height=3, width=20, bg="red", font=("Arial", 12, "bold"))
    close_button.pack(pady=20)

    root.geometry("800x600")
    root.mainloop()


def play_game(game_name):
    if game_name == "سنگ کاغذ قیچی":
        play_rock()
    elif game_name == "مار":
        play_snake()
    elif game_name == "دوز":
        play_doz()

show_game_names()