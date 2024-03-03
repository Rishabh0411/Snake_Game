import pygame
import main
main_menu = False


def draw_menu():
    pass


def draw_game():
    game = main.Game()
    menu_btn = pygame.draw.rect(game.surface, 'light gray', [230, 450, 260, 40], 0, 5)
    pygame.draw.rect(game.surface, 'dark gray', [230, 450, 260, 40], 5, 5)
    text = pygame.font.render('Main Menu', True, 'black')
    game.surface.blit(text, (245, 457))
