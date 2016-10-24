import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

rotation = 1
world_rot = 0


def display():
    global rotation, world_rot

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0.5, 0.5, 0.0)
    glRotate(world_rot, 0.0, 0.0, 1.0)

    # glTranslatef(0.17, 0.17, 0.0)
    # glRotate(rotation, 0.0, 0.0, 1.0)
    # glTranslatef(-0.17, -0.17, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.5, 0.9)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()

    rotation += 5.0
    world_rot += -1.0
    rotation %= 360
    world_rot %= 360
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutCreateWindow('Rotating triangles')
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()
