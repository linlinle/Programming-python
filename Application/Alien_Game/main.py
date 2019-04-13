# -*- coding: utf-8 -*-

import Application.Alien_Game.game_functions as gf
import pygame
from Application.Alien_Game.button import Button
from Application.Alien_Game.game_stats import GameStats
from Application.Alien_Game.scoreboard import Scoreboard
from Application.Alien_Game.settings import Settings
from pygame.sprite import Group

from Application.Alien_Game.ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien_Game Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    ship = Ship(ai_settings,screen)
    aliens = Group()
    bullets = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()