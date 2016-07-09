#!/bin/env python

from __future__ import unicode_literals

import pygame
from util import collision

white_color = pygame.Color(255, 255, 255)


class Drawable(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def draw(self, surface):
        raise NotImplemented


class Player(Drawable):
    def __init__(self, x, y, name):
        super(Player, self).__init__(x, y)
        self._name = name

    def draw(self, surface):
        pygame.draw.rect(surface, white_color, (self._x, self._y, 20, 100))

    def move_down(self, surface):
        if self._y + 15 < surface.get_height():
            self._y += 15

    def move_up(self, surface):
        if self._y - 15 >= 0:
            self._y -= 15

    def intersects(self, ball):
        return collision(self._x, self._y, 20, 100, ball._x, ball._y, 15)


class Opponent(Drawable):
    def __init__(self, x, y):
        super(Opponent, self).__init__(x, y)
        self._name = 'Computer'

    def draw(self, surface):
        pygame.draw.rect(surface, white_color, (self._x, self._y, 20, 100))


class Ball(Drawable):
    def __init__(self, x, y):
        super(Ball, self).__init__(x, y)
        self._radius = 15
        self._dir_x = 1
        self._dir_y = 1

    def draw(self, surface):
        w_width, w_height = surface.get_width(), surface.get_height()
        if self._x + self._radius >= w_width or self._x - self._radius <= 0:
            self._dir_x *= -1
        if self._y + self._radius >= w_height or self._y - self._radius <= 0:
            self._dir_y *= -1
        self._x, self._y = self._x + (self._dir_x * 5), self._y + (self._dir_y * 5)
        pygame.draw.circle(surface, white_color, (self._x, self._y), self._radius)
