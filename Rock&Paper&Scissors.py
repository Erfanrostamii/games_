import random
import pygame
import sys

pygame.init()
width , height = 1080 , 480
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

    while not game_over:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
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
            if winner == 'You won!':
                rang = (0,250,0)
            elif winner == 'You lost!':
                rang = (250,0,0)
            else:
                rang = BLACK
            winner_text = font.render(winner, True, rang)

            chosse = font.render('press \'r\' for rock , press \'p\' for paper , press \'s\' for scissors', True,(250,0,250))
            khoroj = font.render('press \'q\' for Quit', True , (250,0,250))
            screen.blit(chosse, (10, 10))
            screen.blit(khoroj,(10,50))
            screen.blit(user_choice_text, (50, 150))
            screen.blit(computer_choice_text, (50, 250))
            screen.blit(winner_text, (50, 350))

            pygame.display.update()
            pygame.time.wait(2000)
            user_choice = None
chosse = font.render('press \'r\' for rock , press \'p\' for paper , press \'s\' for scissors', True,WHITE)
screen.blit(chosse,(10,220))
pygame.display.update()
game_loop()