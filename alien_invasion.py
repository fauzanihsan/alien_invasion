import sys

import pygame

import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien = Alien(ai_settings, screen)
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")

    sb = Scoreboard(ai_settings,screen,stats)


    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:

         #Redraw the screen during each pass through the loop
         # screen.fill(ai_settings.bg_color)
         # # ship.blitme()
         # for event in pygame.event.get():
         #     if event.type == pygame.QUIT:
         #        sys.exit()
         # pygame.display.flip()
         gf.check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets)

         if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens,bullets)
            gf.update_aliens(ai_settings, screen,stats,sb, ship, aliens, bullets)



         gf.update_screen(ai_settings, screen,stats,sb, ship,aliens, bullets, play_button)
         bullets.update()






         for bullet in bullets.copy():
             if bullet.rect.bottom <= 0:
                 bullets.remove(bullet)
         print(len(bullets))

run_game()



