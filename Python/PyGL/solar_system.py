import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


width, height = 860, 640

textures = None


def init():
    global textures

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, width, height)
    glOrtho(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glutSwapBuffers()
    glFlush()


def process_keys(key, xx, yy):
    pass


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(500, 200)
    glutCreateWindow('Solar system')
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(process_keys)
    glutSpecialFunc(process_keys)
    init()
    glutMainLoop()