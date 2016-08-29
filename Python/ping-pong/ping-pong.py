#!/bin/env python

from __future__ import unicode_literals

import math
import sys

import pygame
from pygame import locals


def collision(rleft, rtop, width, height, center_x, center_y, radius):
    # complete boundbox of the rectangle
    rright, rbottom = rleft + width / 2, rtop + height / 2

    # bounding box of the circle
    cleft, ctop = center_x - radius, center_y - radius
    cright, cbottom = center_x + radius, center_y + radius

    # trivial reject if bounding boxes do not intersect
    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False  # no collision possible

    # check whether any point of rectangle is inside circle's radius
    for x in (rleft, rleft + width):
        for y in (rtop, rtop + height):
            # compare distance between circle's center point and each point of
            # the rectangle with the circle's radius
            if math.hypot(x - center_x, y - center_y) <= radius:
                return True  # collision detected

    # check if center of circle is inside rectangle
    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True  # overlaid

    return False  # no collision detected


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


pygame.init()

surface = pygame.display.set_mode((640, 480))
fps_clock = pygame.time.Clock()
bg_color = pygame.Color(0, 0, 0)

pygame.display.set_caption('Ping pong by mic4ael')


class PingPong(object):
    def __init__(self):
        self._player = Player(30, 150, 'mic4ael')
        self._opponent = Opponent(595, 150)
        self._ball = Ball(305, 215)
        self._event_handlers = {
            locals.QUIT: self._handle_quit,
            locals.KEYDOWN: self._handle_key
        }

    def run(self):
        while True:
            surface.fill(bg_color)
            for event in pygame.event.get():
                self._handle_event(event)

            if self._player.intersects(self._ball):
                self._ball._dir_x *= -1
            self._redraw()
            pygame.display.update()
            fps_clock.tick(30)

    def _handle_event(self, evt):
        if evt.type in self._event_handlers:
            self._event_handlers[evt.type](evt)

    def _handle_quit(self, evt):
        pygame.quit()
        sys.exit()

    def _handle_key(self, evt):
        if evt.key == locals.K_DOWN:
            self._player.move_down(surface)
        elif evt.key == locals.K_UP:
            self._player.move_up(surface)

    def _redraw(self):
        self._player.draw(surface)
        self._ball.draw(surface)
        self._opponent.draw(surface)


def main():
    game = PingPong()
    game.run()


if __name__ == '__main__':
    main()
