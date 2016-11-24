# -*- coding: UTF-8 -*-

# 1. Pamiętaj o możliwości zmiany perspektywy
#     przy użyciu strzałek
# 2. Nałożenie tekstur
# 3. Ruch kulki według wzoru z instrukcji
# 4. Budowanie sprężyny z nachodzących na siebie kulek

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()


def display():
    pass


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640, 480)
    glutCreateWindow('Spring')
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()