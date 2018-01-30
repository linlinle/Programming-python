# -*- coding: utf-8 -*-

import Book.Alien.game_functions as gf
import pygame
from Book.Alien.button import Button
from Book.Alien.game_stats import GameStats
from Book.Alien.scoreboard import Scoreboard
from Book.Alien.settings import Settings
from pygame.sprite import Group

from Application.Alien.ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
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