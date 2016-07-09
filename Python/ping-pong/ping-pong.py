#!/bin/env python

from __future__ import unicode_literals
import sys

import pygame
from pygame import locals

from objects import Player, Opponent, Ball

pygame.init()

surface = pygame.display.set_mode((640, 480))
fps_clock = pygame.time.Clock()
bg_color = pygame.Color(0, 0, 0)

pygame.display.set_caption('Ping pong by mic4ael')


class PingPong(object):
    """Main class of the game"""

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

